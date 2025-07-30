import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Dummy data
df = px.data.gapminder().query("year == 2007")

# Create the app
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("My First Dash App"),
    dcc.Dropdown(
        id='continent-dropdown',
        options=[{"label": c, "value": c} for c in df['continent'].unique()],
        value='Europe'
    ),
    dcc.Graph(id='life-exp-plot')
])

# Callbacks to update graph
@app.callback(
    dash.dependencies.Output('life-exp-plot', 'figure'),
    [dash.dependencies.Input('continent-dropdown', 'value')]
)
def update_graph(continent):
    filtered = df[df['continent'] == continent]
    fig = px.scatter(
        filtered, x='gdpPercap', y='lifeExp',
        size='pop', color='country', log_x=True
    )
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
