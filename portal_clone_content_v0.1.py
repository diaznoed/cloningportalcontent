from pathlib import Path
import sys
import pandas as pd
from arcgis.gis import GIS, Item
from arcgis.features import FeatureLayerCollection
from arcgis.mapping import WebMap

# Connect to source and target GIS
# Replace credentials with your own or securely load them
source_gis = GIS("https://gisgeo.maps.arcgis.com", "your_username", "your_password")  # <--- Update this with your credentials
target_gis = GIS("https://your-target-gis-url/portal")  # <--- Update this with your target portal URL

# Search for items in the source GIS using one of the filters: tags, title, or owner
# Uncomment the filter you want to use and comment out the others

# Filter by tags
# items_to_clone = source_gis.content.search("tags:test", max_items=10)

# Filter by title
# items_to_clone = source_gis.content.search("title:Sample Map", max_items=10)

# Filter by owner
items_to_clone = source_gis.content.search("owner:api_data_owner", max_items=10)  # <--- Update this with the owner filter you need

# Log details of items to clone
for item in items_to_clone:
    print(f"Cloning item: {item.title} (ID: {item.id})")

# Clone the items into the target GIS with error handling
for item in items_to_clone:
    try:
        cloned_items = target_gis.content.clone_items(items=[item], search_existing_items=False)
        for cloned_item in cloned_items:
            print(f"Cloned item: {cloned_item.title} (Type: {cloned_item.type})")
    except Exception as e:
        print(f"Failed to clone item {item.title} (ID: {item.id}): {e}")

print("Cloning completed!")
