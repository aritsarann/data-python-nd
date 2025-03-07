import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output
from app import app
from apps import scatter_layout, histogram_layout, line_layout, treemap_layout


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Menu", className="display-4"),
        html.Hr(),
        html.P(
            "Please choose", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Scatter Plot", href="/apps/scatter_layout", active="exact"),
                dbc.NavLink("Histogram ", href='/apps/histogram_layout', active="exact"),
                dbc.NavLink('Treemap', href='/apps/treemap_layout', active="exact"),
                dbc.NavLink('LineChart', href='/apps/line_layout', active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/scatter_layout':
        return scatter_layout.layout
    if pathname == '/apps/histogram_layout':
        return histogram_layout.layout                 
    if pathname == '/apps/treemap_layout':
        return treemap_layout.layout
    if pathname == '/apps/line_layout':
        return line_layout.layout
    if pathname == '/':
        return "Please choose a link"
    

if __name__ == '__main__':
    app.run_server(debug=False, port = 8060)
    
#Exercise
# 1. Change menu3 to another graph (Not histogram)
# 2. Add the 4th menu (menu4) link to line graph
