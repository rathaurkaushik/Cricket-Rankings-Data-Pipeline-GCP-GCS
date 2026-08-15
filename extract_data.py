import requests
import csv

url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/batsmen"

params = {"formatType":"odi"}

headers = {
    "x-rapidapi-key": "341772c839msh9688e04eb169e9bp1e804ajsn771806b36550",
    "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com",
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json().get('rank', [])  #Extracting the 'rank' data
    csv_filename = "batsmen_rankings.csv"

    if data:
        field_names = ['rank', 'name', 'country'] # Specify required field names

        # Write data into CSV file with specific columns
        with open(csv_filename, mode= 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=field_names)
            # writer.writeheader()
            for entry in data:
                writer.writerow({field: entry.get(field, '') for field in field_names})
        print(f"Data fetched successfully and written to {csv_filename}")
    else:
        print("No data found from the API.")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")