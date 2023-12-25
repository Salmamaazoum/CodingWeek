# Import
import dash
import pandas as pd
import geopandas as gpd
from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load geojson files
df_dep = gpd.read_file('./plot_function/GeoJson_data/dep_geojson.geojson')
df_regions = gpd.read_file(
    './plot_function/GeoJson_data/regions_geojson.geojson')

# Set 'nom' as index
df_dep = df_dep.set_index('nom')
df_regions = df_regions.set_index('nom')

# Cread figure
fig_map = go.Figure()

# Plot department
fig_dep = px.choropleth(df_dep,
                        geojson=df_dep.geometry,
                        locations=df_dep.index,
                        color='random_color',
                        center={"lat": 48.8534, "lon": 2.3488},
                        projection="mercator")
fig_map.add_traces(fig_dep.data)  # Ad department figure in main figure

# Plot regions
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

                dict(label="Department",
                     method="update",
                     args=[{"visible": [False, True]}]),

                dict(label="Regions",
                     method="update",
                     args=[{"visible": [True, False]}]),
            ],
        )
    ]
)

# Update remaining layout properties of the map figure
fig_map.update_geos(fitbounds="locations", visible=False,
                    projection_type="mercator")
fig_map.update_layout(
    margin={"r": 0, "t": 0, "l": 0, "b": 0}, autosize=False, width=800, height=500)

# Create Dash app
app = dash.Dash()

# Config Dash Layoyt
app.layout = html.Div(
    children=[
        html.H1(children='Map'),
        dcc.Graph(id="fare_vs_age", figure=fig_map)
    ]
)

# Load Map
if __name__ == "__main__":
    app.run_server(debug=True)
