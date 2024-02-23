import pandas as pd
import sys

# loads all flights and groups them into a table by owner
url = "https://s3.amazonaws.com/data.ap.org/projects/2024/private-jet-emissions/all_flights_2023.json"


df = pd.read_json(url)

n = df.groupby('tail_number').agg({'icao24': 'count', 'owner': 'first'} ).reset_index().sort_values(by = 'icao24', ascending = False)
n.columns = ['tail_number', 'flights', 'owner']
n['flights_per_month'] = round(n.flights / 12, 1)


# Write to CSV
n.to_csv(sys.stdout)

