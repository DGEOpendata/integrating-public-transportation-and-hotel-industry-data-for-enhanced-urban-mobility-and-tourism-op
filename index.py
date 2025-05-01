python
import pandas as pd

# Load datasets
transport_data = pd.read_csv('public_transportation_usage.csv')
hotel_data = pd.read_excel('Abu_Dhabi_Hotels_Open_Datasets1_0.xlsx')

# Merge datasets on a common attribute, such as date
combined_data = pd.merge(transport_data, hotel_data, on='date', how='inner')

# Analyze peak tourist seasons and transportation usage
peak_seasons = combined_data[combined_data['occupancy_rate'] > 80]
peak_transport_usage = peak_seasons.groupby('route').sum()['ridership']

# Output analysis results
print("Peak Tourist Seasons and Transport Usage:")
print(peak_transport_usage)

# Example of optimizing transit schedule based on peak seasons
optimized_schedule = peak_transport_usage.apply(lambda x: 'Increase frequency' if x > 1000 else 'Maintain frequency')

print("Optimized Transit Schedule Recommendations:")
print(optimized_schedule)
