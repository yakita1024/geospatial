# Import libraries
import os
import pandas as pd
import geopandas as gpd

# Set path
project_dir = r'C:\project'

# Chane for development branch
# Read shapefile
test_gdf = gpd.read_file(os.path.join(project_dir, 'test.shp'))
