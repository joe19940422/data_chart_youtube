# import pandas as pd
# import os
# import glob
#
# # Specify the folder containing the CSV files
# folder_path = '/home/pengfei/Downloads/ins/with_anitta/*.csv'
#
# import pandas as pd
# import os
# import glob
#
# # Create an empty list to store DataFrames
# dataframes = []
#
# # Loop through each CSV file in the folder
# for file_path in glob.glob(folder_path):
#     # Read the CSV file
#     df = pd.read_csv(file_path)
#
#     # Extract artist name from the filename
#     artist_name = os.path.basename(file_path).split('-')[0].capitalize()
#
#     # Add the artist name as a new column
#     df['artist_name'] = artist_name
#
#     # Append the DataFrame to the list
#     dataframes.append(df)
#
# # Concatenate all DataFrames into a single DataFrame
# combined_df = pd.concat(dataframes, ignore_index=True)
#
# # Filter to get only the dates present in Anitta's data
# anitta_dates = combined_df[combined_df['artist_name'] == 'Anitta']['date'].unique()
# filtered_df = combined_df[combined_df['date'].isin(anitta_dates)]
#
# # Pivot the DataFrame with filtered dates
# pivot_df = filtered_df.pivot(index='artist_name', columns='date', values='followers_count')
#
# # Save the pivoted DataFrame to a new CSV file
# pivot_df.to_csv('filtered_pivoted_anitta_stats.csv')
#
# print("Filtered and pivoted CSV saved as 'filtered_pivoted_anitta_stats.csv'")
##################################################################################################################33
import pandas as pd
import os
import glob

# Specify the folder containing the CSV files
folder_path = '/home/pengfei/Downloads/ins/box/*.csv'

# Create an empty list to store DataFrames
dataframes = []

# Loop through each CSV file in the folder
for file_path in glob.glob(folder_path):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Extract artist name from the filename
    artist_name = os.path.basename(file_path).split('-')[0].capitalize()

    # Add the artist name as a new column
    df['artist_name'] = artist_name

    # Append the DataFrame to the list
    dataframes.append(df)

# Concatenate all DataFrames into a single DataFrame
combined_df = pd.concat(dataframes, ignore_index=True)

# Filter to get only the dates present in Anitta's data
# anitta_dates = combined_df[combined_df['artist_name'] == 'Anitta']['date'].unique()
# filtered_df = combined_df[combined_df['date'].isin(anitta_dates)]

# Pivot the DataFrame with filtered dates
pivot_df = combined_df.pivot(index='artist_name', columns='date', values='followers_count')

# Forward fill missing values for each artist
pivot_df = pivot_df.fillna(method='ffill', axis=1)

# Save the pivoted DataFrame to a new CSV file
pivot_df.to_csv('pivoted_box_stats.csv')

print("Filled and pivoted CSV saved as 'filled_pivoted_anitta_stats_1.csv'")
