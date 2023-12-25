# Import
import stats_functions
import geopandas as gpd
import plotly.express as px
import plotly.graph_objects as go

def plot_fr_crime_map():

    # Load data
    df_dep, df_regions = stats_functions.map_plot_data()

    # Get department and regions figures
    fig_dep, fig_regions = get_dep_reg_figures(df_dep, df_regions)

    return fig_dep, fig_regions

def plot_fr_gend_map():

    # Load data
    df_dep, df_regions = stats_functions.map_plot_data_gend()

    # Get department and regions figures
    fig_dep, fig_regions = get_dep_reg_figures_gen(df_dep, df_regions)

    return fig_dep, fig_regions



def get_dep_reg_figures(df_dep, df_regions):

    # Create department figure
    fig_dep = px.choropleth(df_dep,
                    geojson=df_dep.geometry,
                    locations=df_dep.index,
                    color='crimes/1k hab',
                    center={"lat": 48.8534, "lon": 2.3488},
                    projection="mercator",
                    animation_frame='year')

    # Regions layout configuration
    fig_dep.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, autosize=False,width=800,height=500)
    fig_dep.layout.pop("updatemenus")

    # Regions geos configuration
    fig_dep.update_geos(fitbounds="locations", visible=False, projection_type ="mercator")

    # Create regions figure
    fig_regions = px.choropleth(df_regions,
                    geojson=df_regions.geometry,
                    locations=df_regions.index,
                    color='crimes/1k hab',
                    center={"lat": 48.8534, "lon": 2.3488},
                    projection="mercator",
                    animation_frame='year')

    # Department layout configuration
    fig_regions.update_layout(margin={"r":0,"t":0,"l":4,"b":0}, autosize=False,width=800,height=500)
    fig_regions.layout.pop("updatemenus")

    # Department geos configuration
    fig_regions.update_geos(fitbounds="locations", visible=False, projection_type ="mercator")


    return fig_dep, fig_regions


def get_dep_reg_figures_gen(df_dep, df_regions):

    # Create department figure
    fig_dep = px.choropleth(df_dep,
                    geojson=df_dep.geometry,
                    locations=df_dep.index,
                    color='Number of Gendarmerie',
                    center={"lat": 48.8534, "lon": 2.3488},
                    projection="mercator")

    # Regions layout configuration
    fig_dep.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, autosize=False,width=800,height=500)
    fig_dep.layout.pop("updatemenus")

    # Regions geos configuration
    fig_dep.update_geos(fitbounds="locations", visible=False, projection_type ="mercator")

    # Create regions figure
    fig_regions = px.choropleth(df_regions,
                    geojson=df_regions.geometry,
                    locations=df_regions.index,
                    color='Number of Gendarmerie',
                    center={"lat": 48.8534, "lon": 2.3488},
                    projection="mercator")

    # Department layout configuration
    fig_regions.update_layout(margin={"r":0,"t":0,"l":4,"b":0}, autosize=False,width=800,height=500)
    fig_regions.layout.pop("updatemenus")

    # Department geos configuration
    fig_regions.update_geos(fitbounds="locations", visible=False, projection_type ="mercator")


    return fig_dep, fig_regions
