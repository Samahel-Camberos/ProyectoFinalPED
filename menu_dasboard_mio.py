import pandas as pd
import dash
import dash_bootstrap_components as dbc
import graficosprueba1 as d951
from dash import Input, Output, dcc, html

app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY], suppress_callback_exceptions=True)
app.head = [html.Link(rel='stylesheet', href='./custom.css')]

sidebar = html.Div(
    [
        html.H1("Stocks Semanales", className="display-5"),
        html.Hr(),
        html.P(
            "A simple sidebar layout with navigation links", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Dashboard 1", href="/page-1", active="exact"),
                dbc.NavLink("Page 2", href="/page-2", active="exact"),
                dbc.NavLink("Dashboard 3", href="/db3", active="exact"),
                dbc.NavLink("Github", href="https://github.com/", target="_blank", active="exact")
            ],
            vertical=True,
            pills=True
        ),
    ],
    className="SIDEBAR_STYLE",
)

content = html.Div(id="page-content", className="CONTENT_STYLE")

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.P("This is the content of the home page!")
    elif pathname == "/page-1":
        return html.P("This is the content of page 1. Yay!")
    elif pathname == "/page-2":
        return html.P("Oh cool, this is page 2!")
    elif pathname =="/db3":
        data = pd.read_csv("dataset/amazon_12.csv")
        return d951.dashboard(data)
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


if __name__ == "__main__":
    app.run_server(debug=True)