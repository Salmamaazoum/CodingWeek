# Import
import json
from urllib.request import urlopen
import numpy as np
import geopandas as gpd
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from plotly.subplots import make_subplots

# Dowload geojson
df_dep = gpd.read_file(
    'C:/Users/raaro/OneDrive/Documentos/CS/1º Semestre/Coding Weeks/coding-week-2-project/plot_function/GeoJson_data/dep_geojson.geojson')
df_regions = gpd.read_file(
    'C:/Users/raaro/OneDrive/Documentos/CS/1º Semestre/Coding Weeks/coding-week-2-project/plot_function/GeoJson_data/regions_geojson.geojson')

# Set 'nom' as index
df_dep = df_dep.set_index('nom')
df_regions = df_regions.set_index('nom')

# Plot part
fig_map = go.Figure()

# Plot department
fig_dep = px.choropleth(df_dep,
                        geojson=df_dep.geometry,
                        locations=df_dep.index,
                        color='random_color',
                        center={"lat": 48.8534, "lon": 2.3488},
                        projection="mercator")
fig_map.add_traces(fig_dep.data)  # Ad department figure in main figure

# Plot Regions
fig_regions = px.choropleth(df_regions,
                            geojson=df_regions.geometry,
                            locations=df_regions.index,
                            color='random_color',
                            center={"lat": 48.8534, "lon": 2.3488},
                            projection="mercator")
fig_map.add_traces(fig_regions.data)  # Ad regions figure in main figure

# Add buttons
fig_map.update_layout(
    updatemenus=[
        dict(
            type="dropdown",
            buttons=[

                dict(label="Regions",
                     method="update",
                     args=[{"visible": [False, True]}]),

                dict(label="Department",
                     method="update",
                     args=[{"visible": [True, False]}]),
            ],
        )
    ]
)

# Update remaining layout properties
fig_map.update_geos(fitbounds="locations", visible=False,
                    projection_type="mercator")
fig_map.update_layout(
    margin={"r": 0, "t": 0, "l": 0, "b": 0}, autosize=False, width=800, height=500)
fig_map.show()
