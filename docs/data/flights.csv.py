import pandas as pd
import sys

# loads all flights
url = "https://s3.amazonaws.com/data.ap.org/projects/2024/private-jet-emissions/all_flights_2023.json"
df = pd.read_json(url)

# groups them into a table by owner
ppl = df.groupby('owner').agg({'icao24': 'count', 'flight_time': 'sum'} ).reset_index().sort_values(by = 'icao24', ascending = False)
ppl.columns = ['owner', 'flights', 'total_time']
ppl['flights_per_month'] = round(ppl.flights / 12, 1)
ppl['total_time_hrs'] = round(ppl.total_time / 60, 1)


# Write to CSV
ppl.to_csv(sys.stdout)

