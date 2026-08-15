import requests
import csv
from google.cloud import storage


url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/batsmen"

params = {"formatType":"odi"}

headers = {
	"x-rapidapi-key": "341772c839msh9688e04eb169e9bp1e804ajsn771806b36550",
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json().get('rank', []) #Extracting the 'rank' data

    if data:
        field_names = ['rank', 'name', 'country'] # Specify required field names
        csv_filename = "batsmen_rankings.csv"
        # Write data into CSV file with specific columns
        with open(csv_filename, mode= 'w', newline='', encoding='utf-8') as csv_file:

            writer = csv.DictWriter(csv_file, fieldnames = field_names)
            # writer.writeheader()
            for entry in data:
                writer.writerow({field: entry.get(field, '') for field in field_names})

        print(f"Data fetched successfully and written to {csv_filename}")

        # Upload file to GCS bucket
        bucket_name = "cricket-ranking-data-de"
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        destination_blob_name = f'{csv_filename}' # The path to store in GCS bucket

        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(csv_filename)

        print(f"File {csv_filename} uploaded to GCS bucket {bucket_name} as {destination_blob_name}")
    else:
        print("No data found from the API.")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
