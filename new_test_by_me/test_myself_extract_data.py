import requests
import csv

url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/batsmen"

params = {"formatType":"test"}

headers = {
    "x-rapidapi-key": "341772c839msh9688e04eb169e9bp1e804ajsn771806b36550",
    "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json().get('rank', [])  # Extract data from 'rank' key
    csv_file_name = "new_batsman_rank.csv"

    if data:
        field_names = ['id', 'rank', 'name', 'country', 'trend']  # Specify required field names

        with open(csv_file_name, mode='w', newline='', encoding='utf-8') as file_name:
            writer = csv.DictWriter(file_name, fieldnames=field_names)
            writer.writeheader()  # Write header to CSV file
            for entry in data:
                writer.writerow({field: entry.get(field, '') for field in field_names})
        print(f"Data fetched successfully and written to {csv_file_name}")
    else:
        print("No data found from the API.")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")