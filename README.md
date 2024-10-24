# cloningportalcontent
This Python script automates the process of cloning items (such as maps, layers, and other content) from one ArcGIS Online or Portal instance to another. 

Here is a GitHub description for your sanitized script:

---

### ArcGIS Item Cloning Script

**Description**:  
This Python script automates the process of cloning items (such as maps, layers, and other content) from one ArcGIS Online or Portal instance to another. It leverages the ArcGIS API for Python to search for content on a source GIS and clone it to a target GIS environment. The script includes error handling to ensure that any issues encountered during the cloning process are logged.

**Features**:
- Connects to both source and target ArcGIS instances using credentials.
- Allows filtering of items to clone by **tags**, **title**, or **owner**.
- Clones the items into the target ArcGIS environment.
- Logs details of cloned items and errors encountered during the process.

**Usage**:
1. **Update Credentials**: Replace the placeholder credentials (`your_username`, `your_password`) and the GIS portal URLs (`https://your-target-gis-url/portal`) with your actual login information and target GIS portal URL.
2. **Select Filter**: Choose how to filter the items to clone (by tags, title, or owner). Uncomment the filter you wish to use and comment out the others.
3. **Run the Script**: Once configured, the script will search for items matching your filter criteria, log the details of the items being cloned, and attempt to clone them to the target GIS. Any errors will be printed to the console.

**Example**:
```python
source_gis = GIS("https://gisgeo.maps.arcgis.com", "your_username", "your_password")
target_gis = GIS("https://your-target-gis-url/portal")
items_to_clone = source_gis.content.search("owner:api_data_owner", max_items=10)
```

**Requirements**:
- Python 3.x
- `arcgis` package (ArcGIS API for Python)

**Installation**:
To install the required ArcGIS Python package, use:
```bash
pip install arcgis
```

**Notes**:
- Ensure that you have the proper credentials and permissions to access both the source and target GIS environments.
- The cloning process can be adjusted to handle more items or different types of content by modifying the search filters.

---
