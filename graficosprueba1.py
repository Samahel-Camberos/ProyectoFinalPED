import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, dash_table

def infoinicio():
    return html.Div(
        style={"backgroundColor": "black", "color": "white", "textAlign": "center", "fontSize": "20px", "padding": "50px"},
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

def load_data():
    return pd.read_csv("datasets/concatenado.csv")

# Dashboard 1
def total_opiniones():
    data1 = load_data()
    total_opiniones_por_pagina = data1.groupby("paguina web")["opiniones"].sum().reset_index()
    total_opiniones_por_pagina = total_opiniones_por_pagina.sort_values(by='opiniones', ascending=True)
    fig = px.bar(total_opiniones_por_pagina, x="paguina web", y="opiniones",
                 title="<b>Total de Opiniones por Página Web </b>",
                 color="paguina web", barmode="group")

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

def distribucion_calificaciones():
    data1 = load_data()
    fig = px.histogram(data1, x="calificasion", nbins=20,
                       title="<b>Distribución de Calificaciones</b>",
                       labels={"calificasion": "Calificación"})
    fig.update_layout(
        paper_bgcolor="black",
        plot_bgcolor="black",
        font_color="white",
        title_font_color="white",
        title_x=0.5
    )
    return dcc.Graph(figure=fig)

def vista_dataframe():
    data1 = load_data()
    return html.Div([
        html.P(
            "Datos obtenidos mediante web scraping",
            style={'textAlign': 'center', 'font-weight': 'bold', 'fontSize': '24px', 'color': 'white'}
        ),
        dash_table.DataTable(
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



# Dashboard 2
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
    fig = px.pie(conteo_genero_pagina, values="count", names="genero", title="<b>Productos por Género y Página Web</b>")
    fig.update_layout(
        paper_bgcolor="black",
        plot_bgcolor="black",
        font_color="white",
        title_font_color="white",
        title_x=0.5
    )
    return dcc.Graph(figure=fig)

# Dashboard 3
def distribucion_precios():
    data1 = load_data()
    fig = px.histogram(data1, x="precios", nbins=20,
                       title="<b>Distribución de Precios</b>",
                       labels={"precios": "Precio"})
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
    fig = px.scatter(
        data1,
        x="calificasion",
        y="precios",
        title="<b>Relación entre Precio y Calificación</b>",
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

def boxplot_precios():
    data1 = load_data()
    precios_por_pagina = data1.groupby("paguina web")["precios"].mean().reset_index()
    fig = px.bar(precios_por_pagina, x="paguina web", y="precios",
                 title="<b>Precios Promedio por Página Web</b>",
                 labels={"paguina web": "Página Web", "precios": "Precio Promedio"})
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
