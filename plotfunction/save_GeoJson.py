# Import
import numpy as np
import geopandas as gpd
from urllib.request import urlopen

#  GeoJson from French (french department)
url = "https://www.data.gouv.fr/fr/datasets/r/90b9341a-e1f7-4d75-a73c-bbc010c7feeb"
df_dep = gpd.read_file(url)  # Read file with geopandas
df_dep['random_color'] = np.random.randint(
    1, 6, df_dep.shape[0])  # Input Color in a random way

#  GeoJson from French (french region)
url = "https://france-geojson.gregoiredavid.fr/repo/regions.geojson"
df_regions = gpd.read_file(url)  # Read file with geopandas
df_regions['random_color'] = np.random.randint(
    1, 6, df_regions.shape[0])  # Input Color in a random way
# Drop far lands
df_regions = df_regions.drop(9)
df_regions = df_regions.drop(10)
df_regions = df_regions.drop(11)
df_regions = df_regions.drop(12)
df_regions = df_regions.drop(13)

# Save df
df_regions.to_file('GeoJson_data/regions_geojson.geojson')
df_dep.to_file('GeoJson_data/dep_geojson.geojson')
