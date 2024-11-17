import pandas as pd
import numpy as np

# Load the CSV file containing the artist name and follower history
data = pd.read_csv('/home/pengfei/projects/data_chart_youtube/instagram/pivoted_bp_stats.csv')
# Set 'artist_name' as the index
data.set_index('artist_name', inplace=True)


# Function to fill missing values based on historical trend
def fill_missing_values_historically(row):
    # Get the non-missing data points (dates with known follower counts)
    known_data = row.dropna()

    if len(known_data) > 1:
        # Calculate daily rate of change in follower count
        diffs = known_data.diff().dropna()  # Get daily changes

        # Estimate the average daily change (growth rate) over the available period
        avg_daily_growth = diffs.mean()  # Average daily growth

        # Use this growth rate to fill the missing values
        for date in row.index:
            if pd.isna(row[date]):  # If the value is missing
                # Calculate missing value based on last known value and average growth
                last_known_date = known_data[known_data.index <= date].last_valid_index()
                if pd.notna(last_known_date):  # Ensure we found a last known date
                    last_known_value = row[last_known_date]
                    # Estimate the missing value as last known value + average growth * days
                    days_since_last_known = (pd.to_datetime(date) - pd.to_datetime(last_known_date)).days
                    row[date] = last_known_value + avg_daily_growth * days_since_last_known
    else:
        # If not enough data to predict, just fill with the mean of the row
        row.fillna(row.mean(), inplace=True)

    return row


# Apply the function to each artist's row
data_filled = data.apply(fill_missing_values_historically, axis=1)

# Save the filled data to a new CSV
data_filled.to_csv('instagram_data_filled.csv')

# Print the filled data for inspection
print(data_filled)