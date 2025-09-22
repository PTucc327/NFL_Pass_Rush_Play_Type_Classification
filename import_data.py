import nfl_data_py as nfl
import pandas as pd

years = [2023,2024]
data = nfl.import_pbp_data(years, downcast=True, cache=False, alt_path=None)

df = pd.DataFrame(data)
df.to_csv('data.csv', index=False)
print(df)