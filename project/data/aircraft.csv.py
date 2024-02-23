import pandas as pd
import sys

url = "https://s3.amazonaws.com/data.ap.org/projects/2024/private-jet-emissions/all_flights_2023.json"
df = pd.read_json(url)

# select the 20 most popular aircraft models
a = df.groupby(['manufacturername', 'model']).size().reset_index().sort_values(by=0, ascending = False).head(20)
a.columns = ['manufacturer', 'model', '2023 flights']

a.to_csv(sys.stdout, index = False)