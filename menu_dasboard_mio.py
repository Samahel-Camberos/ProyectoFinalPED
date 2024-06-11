import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
import graficosprueba1 as d951

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY], suppress_callback_exceptions=True)


sidebar = html.Div(
    [
        html.H1("Proyecto Final", className="display-5"),
        html.Hr(),
        html.P(
            "Menu de graficos obtenidos", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Inicio", href="/", active="exact"),
                dbc.NavLink("Total Opiniones", href="/total-opiniones", active="exact"),
                dbc.NavLink("Ventas por Género", href="/ventas-genero", active="exact"),
                dbc.NavLink("Productos por Género", href="/productos-genero", active="exact"),
                dbc.NavLink("Promedio Calificaciones", href="/promedio-calificaciones", active="exact"),
                dbc.NavLink("Relación Precio-Calificación", href="/relacion-precio-calificacion", active="exact"),
                dbc.NavLink("Github", href="https://github.com/Samahel-Camberos/ProyectoFinalPED", target="_blank", active="exact")
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
        return d951.infoinicio()
    elif pathname == "/total-opiniones":
        return d951.total_opiniones()
    elif pathname == "/ventas-genero":
        return d951.ventas_genero()
    elif pathname == "/productos-genero":
        return d951.productos_genero()
    elif pathname == "/promedio-calificaciones":
        return d951.promedio_calificaciones()
    elif pathname == "/relacion-precio-calificacion":
        return d951.relacion_precio_calificacion()
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

