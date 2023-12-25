# Import
import os
import dash
import webbrowser
from utils import *
import pandas as pd
import functions_plot
import stats_functions
import tweet_statistics
import geopandas as gpd
import plotly.express as px
from threading import Timer
from functions_stats import *
import plotly.graph_objects as go
from jupyter_dash import JupyterDash
from plotly.tools import mpl_to_plotly
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output

# Get data/figs
fig_dep, fig_regions = functions_plot.plot_fr_crime_map() # Get crime maps figs
fig_dep_gen, fig_regions_gen = functions_plot.plot_fr_gend_map() # Get gendarmerie maps figs
df_dep, df_regions = stats_functions.map_plot_data_nubtotal() # Get crime histogram data

# Create app
app = JupyterDash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Difine app layout
app.layout = dbc.Container(
    [
        # 1º row
        dbc.Row(dbc.Col(html.H2('Crime in France',className='text-center text-primary, mb-3'))),  # Header row

        # 2º row
        dbc.Row(
            [
                # 2º row 1º column (Crime per Location)
                dbc.Col(
                    [
                        html.H5('Crime per Location', className='text-center'), # Header of the field
                        dcc.Dropdown( # Build dropdown dropdown_1_id
                            id='dropdown_1_id', # Define dropdown id
                            options=["Department", "Regions"], # Define dropdown options
                            value='Department', # Define dropdown initial value
                            optionHeight=25,
                            style={'width': '50%'},
                            multi=False
                        ),
                        dcc.Graph( # Build graph 1c2r
                            id='1c2r', # Define graph id
                            figure=fig_dep, # Define graph initial plot
                            style={'height': 550}
                        )
                    ],
                    width='auto' # Set field width
                ),

                # 2º row 2º column
                dbc.Col(
                    [
                        html.H5('Gendarmerie per Location',className='text-center'), # Header of the field
                        dcc.Graph( # Build graph 2c2r
                            id='2c2r', # Define graph id
                            figure=fig_dep_gen, # Define graph initial plot
                            style={'height': 550}
                        )
                    ],
                    width='auto' # Set field width
                ),
            ]
        ),

        # 3º row
        dbc.Row(
            [
                # 3º row 3º column
                dbc.Col(
                    [
                        html.H5('Number of crimes per location',className='text-center'), # Header of the field
                        dcc.Dropdown( # Build dropdown dropdown_2_id
                            id='dropdown_2_id', # Define dropdown id
                            value='Ain', # Define dropdown initial value
                            optionHeight=25,
                            style={'width': '100%'},
                        ),
                        dcc.Graph( # Build graph 1c3r
                            id='1c3r' # Define graph id
                        ),
                    ],
                    width='auto' # Set field width
                )
            ]
        )
    ],
    fluid=True
)


# Callbacks

# Update figure 1c2r via dropdown_1_id
@app.callback(
    Output("1c2r", "figure"),
    Input("dropdown_1_id", "value"))
def display_animated_graph(selection):

    animations = {
        'Department': fig_dep,
        'Regions': fig_regions,
    }

    return animations[selection]

# Update figure 2c2r via dropdown_1_id
@app.callback(
    Output("2c2r", "figure"),
    Input("dropdown_1_id", "value"))
def display_animated_graph(selection):

    animations = {
        'Department': fig_dep_gen,
        'Regions': fig_regions_gen,
    }

    return animations[selection]

# Udate dropdown_2_id options when dropdown_1_id changes
@app.callback(
    Output('dropdown_2_id', 'options'),
    [Input('dropdown_1_id', 'value')])
def update_date_dropdown(selection):

    animations = {
        'Department': [{'label': x, 'value': x} for x in list(df_dep.index.unique())+['France']],
        'Regions': [{'label': x, 'value': x} for x in list(df_regions.index.unique())+['France']],
    }

    return animations[selection]

# Update dropdown_2_id value when dropdown_1_id value changes
@app.callback(
    Output('dropdown_2_id', 'value'),
    [Input('dropdown_1_id', 'value')])
def update_date_dropdown_inicial_value(selection):

    name = {
        'Department': 'Ain',
        'Regions': 'Normandie',
    }

    return name[selection]

# Update figure 1c3r via dropdown_2_id and dropdown_1_id values
@app.callback(
    Output('1c3r', 'figure'),
    [Input('dropdown_2_id', 'value'), Input("dropdown_1_id", "value")])
def name_to_figure(selection, selection_1):

    # Change dataframe based on selection and selection_1
    if selection == 'France':
        df = df_regions.reset_index().groupby(['year']).sum().reset_index() # Sum France results

    elif selection_1 == 'Department':
        df = df_dep.loc[selection] # Filter data by Department

    elif selection_1 == 'Regions':
        df = df_regions.loc[selection] # Filter data by Regions

    # Build figure
    figure = go.Figure()

    # Difine figure layout
    figure.update_layout(
        plot_bgcolor="#FDFEFE",  # set chart bar color
        paper_bgcolor="#FDFEFE",  # Set background chart color
        autosize=False,
        width=600,  # Set chart width
        height=400, # Set chart height
        margin=dict(l=0, r=0, t=0, b=0), # Set chart margin
        font=dict(family="sans-serif",color="#17202A") # Set font
    )

    # Add Bar
    figure.add_trace(go.Bar(x=df["year"], y=df["nº crimes"], marker_color="#F05331"))

    return figure


# Run app
def open_browser():
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new('http://127.0.0.1:1222/')

if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run_server(debug=True, port=1222)

# if __name__ == "__main__":
#     app.run_server(debug=True, port=8058)