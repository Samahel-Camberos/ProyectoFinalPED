import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, dash_table, Dash


def load_data():
    return pd.read_csv("dataset/concatenado.csv")


def infoinicio():
    return html.Div(
        style={"backgroundColor": "black", "color": "white", "textAlign": "center", "fontSize": "20px",
               "padding": "50px"},
        children=[
            html.H1("Trabajo Final", className="display-5", style={"fontSize": "50px", "color": "red"}),
            html.Hr(),
            html.P("Realizado por:", style={"color": "red"}),
            html.Ul(
                style={"listStyleType": "none", "padding": 0},
                children=[
                    html.Li("Arellano Reyes David Alfonzo"),
                    html.Li("Armienta Suarez Brenda Syan"),
                    html.Li("Camberos Galindo Miguel Samahel"),
                    html.Li("López Hernández Ixel Alexa"),
                    html.Li("Ramírez Solís Karla Guadalupe"),
                ]
            ),
            html.H2("Objetivos", style={"fontSize": "40px", "color": "red"}),
            html.H3("Objetivo general", style={"fontSize": "30px", "color": "red"}),
            html.P(
                "El objetivo general del proyecto es aplicar los conocimientos adquiridos durante el semestre en la materia de programación de datos para desarrollar un sistema de análisis de datos eficaz. Este sistema permitirá extraer, limpiar, organizar y visualizar datos de una página web seleccionada, brindando una visión detallada de las tendencias y patrones del mercado en cuestión."
            ),
            html.H3("Objetivos específicos", style={"fontSize": "30px", "color": "red"}),
            html.Ul(
                style={"textAlign": "left", "margin": "0 auto", "width": "80%"},
                children=[
                    html.Li(
                        "Implementar un proceso de web scraping, para desarrollar y aplicar técnicas de extracción de datos para obtener al menos 300 datos relevantes de una página web específica, relacionados con categorías de productos, precios y tendencias de ventas."
                    ),
                    html.Li(
                        "Aplicar técnicas de limpieza y transformación de datos para eliminar valores nulos e inconsistencias, y normalizar los datos en formatos estándar, asegurando su aptitud para el análisis y presentación"
                    ),
                    html.Li(
                        "Diseñar y desarrollar visualizaciones claras y atractivas, para la presentación de la información obtenida."
                    ),
                ]
            ),
        ]
    )


def total_opiniones():
    data1 = load_data()
    return html.Div([
        dcc.Dropdown(
            id="ddlTotalOpiniones",
            options=[{"label": page, "value": page} for page in data1["paguina web"].unique()],
            value=data1["paguina web"].unique()[0],
            style={
                "backgroundColor": "black",
                "color": "Blue",
                "border": "1px solid blue"
            }
        ),
        dcc.Graph(id="total_opiniones")
    ])


def promedio_calificaciones():
    data1 = load_data()
    return html.Div([
        dcc.Dropdown(
            id="ddlPageRating",
            options=[{"label": page, "value": page} for page in data1["paguina web"].unique()],
            value=data1["paguina web"].unique()[0],
            style={
                "backgroundColor": "black",
                "color": "Blue",
                "border": "1px solid blue"
            }
        ),
        dcc.Graph(id="promedio_calificaciones")
    ])


def distribucion_calificaciones():
    data1 = load_data()
    return html.Div([
        dcc.Dropdown(
            id="ddlPageDistribution",
            options=[{"label": page, "value": page} for page in data1["paguina web"].unique()],
            value=data1["paguina web"].unique()[0],
            style={
                "backgroundColor": "black",
                "color": "Blue",
                "border": "1px solid blue"
            }
        ),
        dcc.Graph(id="distribucion_calificaciones")
    ])


def vista_dataframe():
    data1 = load_data()
    return html.Div([
        html.P(
            "Datos obtenidos mediante web scraping",
            style={'textAlign': 'center', 'font-weight': 'bold', 'fontSize': '24px', 'color': 'white'}
        ),
        dash_table.DataTable(
            id="data_table",
            data=data1.to_dict('records'),
            columns=[{"name": i, "id": i} for i in data1.columns],
            style_table={'overflowX': 'auto'},
            style_header={
                'backgroundColor': 'black',
                'color': 'white'
            },
            style_cell={
                'backgroundColor': 'black',
                'color': 'white'
            },
        )
    ])


def ventas_genero():
    data1 = load_data()
    return html.Div([
        dcc.Dropdown(
            id="ddlCompany",
            options=[
                {"label": "Amazon", "value": "Amazon"},
                {"label": "Mercado Libre", "value": "Mercado Libre"}
            ],
            value="Amazon",
            style={
                "backgroundColor": "black",
                "color": "Blue",
                "border": "1px solid blue"
            }
        ),
        dcc.Graph(id="figVentasGenero")
    ])


def productos_genero():
    data1 = load_data()
    return html.Div([
        dcc.Dropdown(
            id="ddlPage",
            options=[{"label": page, "value": page} for page in data1["paguina web"].unique()],
            value=data1["paguina web"].unique()[0],
            style={
                "backgroundColor": "black",
                "color": "Blue",
                "border": "1px solid blue"
            }
        ),
        dcc.Graph(id="figProductosGenero")
    ])


def distribucion_precios():
    data1 = load_data()
    return html.Div([
        dcc.Dropdown(
            id="ddlPagePrice",
            options=[{"label": page, "value": page} for page in data1["paguina web"].unique()],
            value=data1["paguina web"].unique()[0],
            style={
                "backgroundColor": "black",
                "color": "Blue",
                "border": "1px solid blue"
            }
        ),
        dcc.Graph(id="distribucion_precios")
    ])


def relacion_precio_calificacion():
    data1 = load_data()
    return html.Div([
        dcc.Dropdown(
            id="ddlPageRel",
            options=[{"label": page, "value": page} for page in data1["paguina web"].unique()],
            value=data1["paguina web"].unique()[0],
            style={
                "backgroundColor": "black",
                "color": "Blue",
                "border": "1px solid blue"
            }
        ),
        dcc.Graph(id="relacion_precio_calificacion")
    ])


def boxplot_precios():
    data1 = load_data()
    return html.Div([
        dcc.Dropdown(
            id="ddlPageBoxplot",
            options=[{"label": page, "value": page} for page in data1["paguina web"].unique()],
            value=data1["paguina web"].unique()[0],
            style={
                "backgroundColor": "black",
                "color": "Blue",
                "border": "1px solid blue"
            }
        ),
        dcc.Graph(id="boxplot_precios")
    ])


def register_callbacks(app):
    @app.callback(
        Output("figVentasGenero", "figure"),
        Input("ddlCompany", "value")
    )
    def update_ventas_genero(company):
        data1 = load_data()
        data_filtered = data1[data1['paguina web'].str.lower() == company.lower()].sort_values(by='precios')
        fig = px.bar(data_filtered, x="genero", y="precios", title=f"Ventas {company}")
        fig.update_layout(
            paper_bgcolor="black",
            plot_bgcolor="black",
            font_color="white",
            title_font_color="white",
            title_x=0.5
        )
        return fig

    @app.callback(
        Output("figProductosGenero", "figure"),
        Input("ddlPage", "value")
    )
    def update_productos_genero(page):
        data1 = load_data()
        conteo_genero_pagina = data1[data1['paguina web'] == page].groupby(
            ["paguina web", "genero"]).size().reset_index(name="count")
        fig = px.pie(conteo_genero_pagina, values="count", names="genero",
                     title=f"<b>Productos por Género y Página Web ({page})</b>")
        fig.update_layout(
            paper_bgcolor="black",
            plot_bgcolor="black",
            font_color="white",
            title_font_color="white",
            title_x=0.5
        )
        return fig

    @app.callback(
        Output("distribucion_precios", "figure"),
        Input("ddlPagePrice", "value")
    )
    def update_distribucion_precios(page):
        data1 = load_data()
        data_filtered = data1[data1['paguina web'] == page]
        fig = px.histogram(data_filtered, x="precios", nbins=20,
                           title=f"<b>Distribución de Precios ({page})</b>",
                           labels={"precios": "Precio"})
        fig.update_layout(
            paper_bgcolor="black",
            plot_bgcolor="black",
            font_color="white",
            title_font_color="white",
            title_x=0.5
        )
        return fig

    @app.callback(
        Output("promedio_calificaciones", "figure"),
        Input("ddlPageRating", "value")
    )
    def update_promedio_calificaciones(page):
        data1 = load_data()
        data_filtered = data1[data1['paguina web'] == page]
        promedio_calificaciones = data_filtered.groupby("paguina web")["calificasion"].mean().reset_index()
        fig = px.bar(promedio_calificaciones, x="paguina web", y="calificasion",
                     title=f"<b>Promedio de Calificaciones por Empresa ({page})</b>",
                     color='paguina web', labels={'calificasion': 'Calificación Promedio'})
        fig.update_layout(
            paper_bgcolor="black",
            plot_bgcolor="black",
            font_color="white",
            title_font_color="white",
            title_x=0.5
        )
        return fig

    @app.callback(
        Output("relacion_precio_calificacion", "figure"),
        Input("ddlPageRel", "value")
    )
    def update_relacion_precio_calificacion(page):
        data1 = load_data()
        data_filtered = data1[data1['paguina web'] == page]
        fig = px.scatter(
            data_filtered,
            x="calificasion",
            y="precios",
            title=f"<b>Relación entre Precio y Calificación ({page})</b>",
            labels={"calificasion": "Calificación", "precios": "Precio"},
            hover_data=["nombre", "opiniones"]
        )
        fig.update_layout(
            paper_bgcolor="black",
            plot_bgcolor="black",
            font_color="white",
            title_font_color="white",
            title_x=0.5
        )
        return fig

    @app.callback(
        Output("boxplot_precios", "figure"),
        Input("ddlPageBoxplot", "value")
    )
    def update_boxplot_precios(page):
        data1 = load_data()
        data_filtered = data1[data1['paguina web'] == page]
        precios_por_pagina = data_filtered.groupby("paguina web")["precios"].mean().reset_index()
        fig = px.bar(precios_por_pagina, x="paguina web", y="precios",
                     title=f"<b>Precios Promedio por Página Web ({page})</b>",
                     labels={"paguina web": "Página Web", "precios": "Precio Promedio"})
        fig.update_layout(
            paper_bgcolor="black",
            plot_bgcolor="black",
            font_color="white",
            title_font_color="white",
            title_x=0.5
        )
        return fig

    @app.callback(
        Output("total_opiniones", "figure"),
        Input("ddlTotalOpiniones", "value")
    )
    def update_total_opiniones(page):
        data1 = load_data()
        total_opiniones_por_pagina = data1[data1['paguina web'] == page].groupby("paguina web")["opiniones"].sum().reset_index()
        total_opiniones_por_pagina = total_opiniones_por_pagina.sort_values(by='opiniones', ascending=True)
        fig = px.bar(total_opiniones_por_pagina, x="paguina web", y="opiniones",
                     title=f"<b>Total de Opiniones por Página Web ({page})</b>",
                     color="paguina web", barmode="group")
        fig.update_layout(
            paper_bgcolor="black",
            plot_bgcolor="black",
            font_color="white",
            title_font_color="white",
            title_x=0.5
        )
        return fig

    @app.callback(
        Output("distribucion_calificaciones", "figure"),
        Input("ddlPageDistribution", "value")
    )
    def update_distribucion_calificaciones(page):
        data1 = load_data()
        data_filtered = data1[data1['paguina web'] == page]
        fig = px.histogram(data_filtered, x="calificasion", nbins=20,
                           title=f"<b>Distribución de Calificaciones ({page})</b>",
                           labels={"calificasion": "Calificación"})
        fig.update_layout(
            paper_bgcolor="black",
            plot_bgcolor="black",
            font_color="white",
            title_font_color="white",
            title_x=0.5
        )
        return fig


app = Dash(__name__, external_stylesheets=[dbc.themes.SLATE])
app.layout = html.Div([
    infoinicio(),
    total_opiniones(),
    promedio_calificaciones(),
    distribucion_calificaciones(),
    vista_dataframe(),
    ventas_genero(),
    productos_genero(),
    distribucion_precios(),
    relacion_precio_calificacion(),
    boxplot_precios()
])

register_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)
