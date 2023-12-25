#évolution des crimes pour chaque département en fonction des années curseur sur le département

import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
from functions_stats import *

# load dataset example
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/volcano.csv")
df = px.data.tips()

# create figure
fig = go.Figure()

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

df = right_dictionnary(1)

# plot histogram
fig = px.histogram(df, x="years", y="crimes")

# change size of the chart
fig.update_layout(
    width=800,
    height=900,
    autosize=False,
    margin=dict(t=100, b=0, l=0, r=0),
)

# creating the department list
L = []
for i in range(1,97):
                
            L.append(dict(
                label=str(i),
                method="update",
                args=["df", right_dictionnary(i)]
                )
            )

# Add dropdown
#fig.update_layout(
    
updatemenus=[
    dict(
        buttons=list(
            L
        ),
        direction="down",
        pad={"r": 10, "t": 10},
        showactive=True,
        x=-1,
        xanchor="left",
        y=1.1,
        yanchor="top"
   ),
]    
#)

layout['updatemenus'] = updatemenus
fig.show()