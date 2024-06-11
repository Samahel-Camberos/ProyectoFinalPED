import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
import graficosprueba1 as d951

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY], suppress_callback_exceptions=True)

# Sidebar layout
sidebar = html.Div(
    [
        html.H1("Proyecto Final", className="display-5"),
        html.Hr(),
        html.P("Menu de graficos obtenidos", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("Inicio", href="/", active="exact"),
                dbc.NavLink("Visualización de datos", href="/visualizacion-datos", active="exact"),  # Nueva entrada
                dbc.NavLink("Dashboard 1", href="/dashboard-1", active="exact"),
                dbc.NavLink("Dashboard 2", href="/dashboard-2", active="exact"),
                dbc.NavLink("Dashboard 3", href="/dashboard-3", active="exact"),
                dbc.NavLink("Github", href="https://github.com/Samahel-Camberos/ProyectoFinalPED/watchers",
                            target="_blank", active="exact")
            ],
            vertical=True,
            pills=True
        ),
    ],
    className="SIDEBAR_STYLE",
)

# Content layout
content = html.Div(id="page-content", className="CONTENT_STYLE")

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

# Callback to render the content based on the current pathname
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return d951.infoinicio()

    elif pathname == "/visualizacion-datos":
        return d951.vista_dataframe()

    elif pathname == "/dashboard-1":
        return dbc.Container([
            dbc.Row([
                dbc.Col(d951.total_opiniones(), width=6),
                dbc.Col(d951.promedio_calificaciones(), width=6)
            ]),
            dbc.Row([
                dbc.Col(d951.distribucion_calificaciones(), width=12)
            ])
        ])
    elif pathname == "/dashboard-2":
        return dbc.Container([
            dbc.Row([
                dbc.Col(d951.ventas_genero(), width=6),
                dbc.Col(d951.productos_genero(), width=6)
            ])
        ])
    elif pathname == "/dashboard-3":
        return dbc.Container([
            dbc.Row([
                dbc.Col(d951.promedio_calificaciones(), width=6),
                dbc.Col(d951.distribucion_precios(), width=6)
            ]),
            dbc.Row([
                dbc.Col(d951.relacion_precio_calificacion(), width=6),
                dbc.Col(d951.boxplot_precios(), width=6)
            ])
        ])
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )

d951.register_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)


