# # 16.6 
# # simplify the loop that extracts earthquake data from the all_eq_dicts list.
# # Before Refactoring:
# magnitudes = []
# longitudes = []
# latitudes = []
# titles = []

# for eq_dict in all_eq_dicts:
#     mag = eq_dict["properties"]["mag"]
#     lon = eq_dict["geometry"]["coordinates"][0]
#     lat = eq_dict["geometry"]["coordinates"][1]
#     title = eq_dict["properties"]["title"]

#     magnitudes.append(mag)
#     longitudes.append(lon)
#     latitudes.append(lat)
#     titles.append(title)
# # After Refactoring:
# # Initializing the Lists
# magnitudes, longitudes, latitudes, titles = [], [], [], []
# # Looping Through the Data
# for eq_dict in all_eq_dicts:
#     # Extracting and Appending Data
#     magnitudes.append(eq_dict["properties"]["mag"])
#     longitudes.append(eq_dict["geometry"]["coordinates"][0])
#     latitudes.append(eq_dict["geometry"]["coordinates"][1])
#     titles.append(eq_dict["properties"]["title"])

# 16.9
import csv
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Read the fire data from the CSV file without pandas
fire_data = []
with open("world_fires_1_day.csv", newline='', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        # Only include rows with latitude, longitude, and brightness
        if row['latitude'] and row['longitude'] and row['brightness']:
            fire_data.append({
                'latitude': float(row['latitude']),
                'longitude': float(row['longitude']),
                'brightness': float(row['brightness'])
            })

# Step 2: Set up the map using Matplotlib
fig, ax = plt.subplots(figsize=(15, 10))

# Create a grid for the map (simple world map with latitude and longitude)
ax.set_xlim([-180, 180])  # Longitude limits
ax.set_ylim([-90, 90])  # Latitude limits

# Draw a grid of latitude and longitude
ax.grid(True, which='both', axis='both', color='gray', linestyle='-', linewidth=0.5)

# Draw the outline of the world (basic rectangular world map)
ax.plot([-180, 180], [90, 90], color='black', lw=2)  # Top border
ax.plot([-180, 180], [-90, -90], color='black', lw=2)  # Bottom border
ax.plot([-180, -180], [-90, 90], color='black', lw=2)  # Left border
ax.plot([180, 180], [-90, 90], color='black', lw=2)  # Right border

# Step 3: Plot the fire locations on the map
for fire in fire_data:
    # Plot fire locations using latitude and longitude
    ax.plot(fire['longitude'], fire['latitude'], marker='o', color=plt.cm.viridis(fire['brightness'] / max(f['brightness'] for f in fire_data)), markersize=5, alpha=0.7)

# Step 4: Add a colorbar for brightness
sm = plt.cm.ScalarMappable(cmap='viridis', norm=plt.Normalize(vmin=min(fire['brightness'] for fire in fire_data), vmax=max(fire['brightness'] for fire in fire_data)))
sm.set_array([])  # Empty array for colorbar
plt.colorbar(sm, ax=ax, label='Fire Brightness')

# Step 5: Customize the plot
plt.title('World Fires Map (Brightness)', fontsize=15)
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Show the plot
plt.show()

