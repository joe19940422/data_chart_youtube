import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Provided data
data = {
    'date': [
        "20180615", "20190126", "20200308", "20200507", "20201010", "20201012",
        "20201123", "20210301", "20210410", "20210414", "20210526", "20210716",
        "20210723", "20211021", "20211226", "20230316", "20230502", "20230618",
        "20231128", "20240112", "20240209", "20240323", "20240505", "20241112"
    ],
    'followers': [
        "0", "14m", "30M", "32.6m", "40.3m", "40.4m", "42.5m", "47,3m", "50m",
        "50.4m", "53m", "55.6m", "56m", "64m", "52.9m", "90m", "93m", "95m",
        "99m", "100m", "101m", "102m", "103m", "104939756"
    ]
}

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Convert dates to datetime objects
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')

# Normalize follower counts
def convert_to_numeric(followers_str):
    followers_str = followers_str.lower().replace("m", "e6").replace(",", ".")
    return float(followers_str)

df['followers'] = df['followers'].apply(convert_to_numeric)

# Set the date range for interpolation
start_date = df['date'].min()
end_date = df['date'].max()
full_date_range = pd.date_range(start=start_date, end=end_date)

# Reindex with full date range and interpolate
df_full = df.set_index('date').reindex(full_date_range).interpolate(method='linear')

# Convert the followers column to integers (BigInt compatible)
df_full['followers'] = df_full['followers'].astype(np.int64)

# Reset the index and rename columns
df_full.reset_index(inplace=True)
df_full.columns = ['date', 'followers']

# Show the interpolated data
print(df_full.head())  # Show the first few rows
print(df_full.tail())  # Show the last few rows

# Optionally, save to a CSV file
df_full.to_csv('lisa_instagram_followers_history.csv', index=False)
