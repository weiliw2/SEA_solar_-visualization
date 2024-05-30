import json
import pandas as pd

# Load the original GeoJSON data
geojson_path = '/Users/weilynnw/Desktop/Map/seattle_solar_data.geojson'
with open(geojson_path, 'r') as f:
    geojson_data = json.load(f)

# Function to replace NaN with a default value (0 or null)
def replace_nan(feature):
    for key, value in feature['properties'].items():
        if isinstance(value, float) and pd.isna(value):
            feature['properties'][key] = 0  # Replace NaN with 0
    return feature

# Apply the replacement function to all features
geojson_data['features'] = [replace_nan(feature) for feature in geojson_data['features']]

# Save the processed GeoJSON data
processed_geojson_path = '/Users/weilynnw/Desktop/Map/seattle_solar_data.geojson'
with open(processed_geojson_path, 'w') as f:
    json.dump(geojson_data, f)

print(f"Processed GeoJSON saved to {processed_geojson_path}")
