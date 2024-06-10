import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output



def infoinicio():
    return html.Div(
        style={'backgroundColor': 'black', 'color': 'white', 'textAlign': 'center', 'fontSize': '20px', 'padding': '50px'},
        children=[
            html.H1("Trabajo Final", className="display-5", style={'fontSize': '50px'}),
            html.Hr(),
            html.P("Realizado por:"),
            html.Ul(
                style={'listStyleType': 'none', 'padding': 0},
                children=[
                    html.Li("Arellano Reyes David Alfonzo"),
                    html.Li("Armienta Suarez Brenda Syan"),
                    html.Li("Camberos Galindo Miguel Samahel"),
                    html.Li("López Hernández Ixel Alexa"),
                    html.Li("Ramírez Solís Karla Guadalupe"),
                ]
            ),
            html.H2("Objetivos", style={'fontSize': '40px'}),
            html.H3("Objetivo general", style={'fontSize': '30px'}),
            html.P(
                "El objetivo general del proyecto es aplicar los conocimientos adquiridos durante el semestre en la materia de programación de datos para desarrollar un sistema de análisis de datos eficaz. Este sistema permitirá extraer, limpiar, organizar y visualizar datos de una página web seleccionada, brindando una visión detallada de las tendencias y patrones del mercado en cuestión."
            ),
            html.H3("Objetivos específicos", style={'fontSize': '30px'}),
            html.Ul(
                style={'textAlign': 'left', 'margin': '0 auto', 'width': '80%'},
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


def load_data():
    return pd.read_csv("datasets/concatenado.csv")

def total_opiniones():
    data1 = load_data()
    total_opiniones_por_pagina = data1.groupby("paguina web")["opiniones"].sum().reset_index()
    total_opiniones_por_pagina = total_opiniones_por_pagina.sort_values(by='opiniones', ascending=True)
    fig = px.bar(total_opiniones_por_pagina, x="paguina web", y="opiniones",
                 title="<b>Total de Opiniones por Página Web (Ascendente)</b>",
                 color="paguina web", barmode="group")

    fig.update_layout(
        paper_bgcolor="black",
        plot_bgcolor="black",
        font_color="white",
        title_font_color="white",
        title_x=0.5
    )
    return dcc.Graph(figure=fig)

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
    conteo_genero_pagina = data1.groupby(["paguina web", "genero"]).size().reset_index(name="count")
    fig = px.bar(conteo_genero_pagina, x="count", y="paguina web", color="genero", barmode="group",
                 title="<b>Cantidad de Productos por Género y Página Web</b>",
                 orientation='h', category_orders={"paguina web": ["mercado libre", "amazon"]})
    fig.update_layout(
        paper_bgcolor="black",
        plot_bgcolor="black",
        font_color="white",
        title_font_color="white",
        title_x=0.5
    )
    return dcc.Graph(figure=fig)

def promedio_calificaciones():
    data1 = load_data()
    promedio_calificaciones = data1.groupby("paguina web")["calificasion"].mean().reset_index()
    fig = px.bar(promedio_calificaciones, x="paguina web", y="calificasion",
                 title="<b>Promedio de Calificaciones por Empresa</b>",
                 color='paguina web', labels={'calificasion': 'Calificación Promedio'})

    fig.update_layout(
        paper_bgcolor="black",
        plot_bgcolor="black",
        font_color="white",
        title_font_color="white",
        title_x=0.5
    )
    return dcc.Graph(figure=fig)

def relacion_precio_calificacion():
    data1 = load_data()
    fig = px.scatter(data1, x="calificasion", y="precios",
                     title="<b>Relación entre Precio y Calificación</b>",
                     labels={"calificasion": "Calificación", "precios": "Precio"},
                     trendline="ols", hover_data=['nombre', 'opiniones'])
    fig.update_layout(
        paper_bgcolor="black",
        plot_bgcolor="black",
        font_color="white",
        title_font_color="white",
        title_x=0.5
    )
    return dcc.Graph(figure=fig)

def register_callbacks(app):
    @app.callback(
        Output("figVentasGenero", "figure"),
        Input("ddlCompany", "value")
    )
    def update_ventas_genero(company):
        data1 = load_data()
        data_filtered = data1[data1['paguina web'].str.lower() == company.lower()]
        fig = px.bar(data_filtered, x="genero", y="precios", title=f"Ventas {company}")
        fig.update_layout(
            paper_bgcolor="black",
            plot_bgcolor="black",
            font_color="white",
            title_font_color="white",
            title_x=0.5
        )
        return fig

def relacion_precio_calificacion():
    # Carga el conjunto de datos
    data1 = load_data()


    fig = px.scatter(
        data1,
        x="calificasion",
        y="precios",
        title=" <b>Relación entre Precio y Calificación</b>",
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


    return dcc.Graph(figure=fig)
