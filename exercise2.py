# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash
import plotly.graph_objs as go


# Exercise 2
# Create another visualization of your choice of data and chart type.
# You can use pandas to help loading data, or just hard-coded the data is fine.
# initialize Dash environment

# static data
countries = ['Pakistan','Qatar','Afghanistan','Bangladesh','Egypt']

app = dash.Dash(__name__)

# set up an layout
app.layout = html.Div(children=[
    # H1 title on the page
    html.H1(children='Hello Dash for HCDE 411'),

    # a div to put a short description
    html.Div(children='''
        This is a another Dash application for HCDE 411
    '''),

    # append the visualization to the page
    dcc.Graph(
        id='example-graph',
        figure={
            # configure the data
            'data': [
                # This is how we define a scatter plot. Note that it also uses "go.Scatter",
                # but with the mode to be only "markers"
                go.Scatter(
                    x=['115.7','92.4','86','83.3','73'],
                    y=['204','2','37','168','101'],
                    mode='markers',
                    text=countries,  # This line sets the vehicle name as the points' labels.
                    marker={
                        'size': 10,
                        'opacity': 0.8  # By making the points a bit transparent, it can alleviate the occlusion issue
                    }
                )
            ],
            'layout': {
                'title': 'Car Dataset 2004',
                # It is always a good practice to have axis labels.
                # This is especially important in this case as the numbers are not trivial
                'xaxis': {'title': 'Horse Power'},
                'yaxis': {'title': 'Weight'},
            }
        }
    ),

])

if __name__ == '__main__':
    # start the Dash app
    app.run_server(debug=True)