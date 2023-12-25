import dash
import plotly.graph_objects as go
import plotly.express as px
from functions_stats import *
from utils import *
import pandas as pd
import dash_bootstrap_components as dbc
from jupyter_dash import JupyterDash
from dash import Dash, dcc, html, Input, Output

# Antoine
liste_departement = departement_nom()

# def function to create right dictionnary for each department

def right_dictionnary(i):
    data = nb_crimes_per_depart_per_year()[str(i)]
    df={}
    df["years"]=[]
    df["crimes"]=[]
    for elt in data:
        df["years"].append(elt)
        df["crimes"].append(data[elt])

    df = pd.DataFrame.from_dict(df)
    return df


# Create app
app = JupyterDash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

fig_names = liste_departement['Department'] # list the department name for the dropdown menu
fig_dropdown = html.Div([
        dcc.Dropdown(
        id='fig_dropdown',
        options=[{'label': x, 'value': x} for x in fig_names],
        value="Ain",
        style={'height': '30px', 'width': '600px'} # set size for the dropdown menu
    )])
fig_plot = html.Div(id='fig_plot')
app.layout = dbc.Container(
    # 2º row
        dbc.Row(
            # 2º row 1º column (Crime per Location)
            [dbc.Col([fig_dropdown,fig_plot],width='auto'),]
            )
)



@app.callback(
Output('fig_plot', 'children'),
[Input('fig_dropdown', 'value')])

def name_to_figure(fig_name):
    figure = go.Figure()
    figure.update_layout(
        plot_bgcolor="#FDFEFE", # set chart bar color FDFEFE
        paper_bgcolor="#FDFEFE", # set background chart color
        autosize=False,
        width=600, # set the size of the chart
        height=400,
        margin=dict(l=20, r=20, t=40, b=20),
        title={
            'text': "Number of crime for each department",
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        font=dict(
            family="sans-serif",
            color="#17202A"
        )
    )
    current_department = liste_departement.loc[liste_departement["Department"] == str(fig_name)]["Number"]
    figure.add_trace(go.Bar(x=right_dictionnary(int(current_department))["years"], y=right_dictionnary(int(current_department))["crimes"],marker_color="#F05331")) # change the chart depending of the dropdown menu
    return dcc.Graph(figure=figure)


if __name__ == "__main__":
    app.run_server(debug=True, port=8058)