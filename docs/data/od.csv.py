import pandas as pd
import sys

# loads all flights
url = "https://s3.amazonaws.com/data.ap.org/projects/2024/private-jet-emissions/all_flights_2023.json"
df = pd.read_json(url)

# group by origin and departure
od = df.groupby(['dept_city', 'arrival_city']).size().reset_index().sort_values(by = 0, ascending = False)
od.columns = ['departure', 'arrival', 'flights']
od = od[od.flights >= 20]

# write to csv
od.to_csv(sys.stdout)