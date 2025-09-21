import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point
# --- 1. Synthetic Data Generation ---
# Generate synthetic delivery data
np.random.seed(42) # for reproducibility
num_deliveries = 100
delivery_data = {
    'order_id': range(1, num_deliveries + 1),
    'latitude': np.random.uniform(34, 35, num_deliveries),  # Example lat/long range
    'longitude': np.random.uniform(-118, -117, num_deliveries),
    'delivery_cost': np.random.uniform(5, 20, num_deliveries),
    'distance_km': np.random.uniform(1, 15, num_deliveries)
}
df = pd.DataFrame(delivery_data)
# Create geospatial data
geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")
# --- 2. Data Cleaning and Analysis ---
# (No significant cleaning needed for synthetic data)
# Calculate total delivery cost
total_cost = df['delivery_cost'].sum()
print(f"Total delivery cost: ${total_cost:.2f}")
# Analyze cost distribution
average_cost = df['delivery_cost'].mean()
print(f"Average delivery cost: ${average_cost:.2f}")
# --- 3. Geo-Spatial Analysis and Visualization ---
# Visualize delivery locations
plt.figure(figsize=(10, 6))
gdf.plot(column='delivery_cost', cmap='viridis', legend=True, markersize=20, alpha=0.7)
plt.title('Delivery Locations and Costs')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('delivery_locations.png')
print("Plot saved to delivery_locations.png")
#Example of potential optimization (Illustrative - Requires more sophisticated algorithms for real-world application)
#Sort deliveries by distance to optimize route
df_sorted = df.sort_values('distance_km')
optimized_total_cost = df_sorted['delivery_cost'].sum()
cost_reduction = total_cost - optimized_total_cost
print(f"Potential cost reduction by sorting deliveries by distance: ${cost_reduction:.2f}")
# --- 4. Reporting and Recommendations ---
# (Further analysis and recommendations would be added here in a real-world scenario.  
# This might involve clustering, route optimization algorithms, etc.  
#  The 15% reduction goal would be assessed against the results of more advanced analysis.)
print("Analysis complete.  Note: This is a simplified example.  Real-world route optimization requires more advanced algorithms.")