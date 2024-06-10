import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output

def load_data():
    return pd.read_csv("datasets/concatenado.csv")

def total_opiniones():
    data1 = load_data()
    total_opiniones_por_pagina = data1.groupby("paguina web")["opiniones"].sum().reset_index()
    total_opiniones_por_pagina = total_opiniones_por_pagina.sort_values(by='opiniones', ascending=True)
    fig = px.bar(total_opiniones_por_pagina, x="paguina web", y="opiniones",
                 title="Total de Opiniones por Página Web (Ascendente)",
                 color="paguina web", barmode="group")

    fig.update_layout(
        paper_bgcolor="black",
        plot_bgcolor="black",
        font_color="white",
        title_font_color="white"
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
                "color": "white",
                "border": "1px solid grey"
            }
        ),
        dcc.Graph(id="figVentasGenero")

    ])

def productos_genero():
    data1 = load_data()
    conteo_genero_pagina = data1.groupby(['paguina web', 'genero']).size().reset_index(name='count')
    fig = px.bar(conteo_genero_pagina, x="count", y="paguina web", color="genero", barmode="group",
                 title="Cantidad de Productos por Género y Página Web",
                 orientation='h', category_orders={"paguina web": ["mercado libre", "amazon"]})
    fig.update_layout(
        paper_bgcolor="black",
        plot_bgcolor="black",
        font_color="white",
        title_font_color="white"
    )
    return dcc.Graph(figure=fig)

def promedio_calificaciones():
    data1 = load_data()
    promedio_calificaciones = data1.groupby('paguina web')['calificasion'].mean().reset_index()
    fig = px.bar(promedio_calificaciones, x='paguina web', y='calificasion',
                 title="Promedio de Calificaciones por Empresa",
                 color='paguina web', labels={'calificasion': 'Calificación Promedio'})

    fig.update_layout(
        paper_bgcolor="black",
        plot_bgcolor="black",
        font_color="white",
        title_font_color="white"
    )
    return dcc.Graph(figure=fig)

def relacion_precio_calificacion():
    data1 = load_data()
    fig = px.scatter(data1, x='calificasion', y='precios',
                     title="Relación entre Precio y Calificación",
                     labels={'calificasion': 'Calificación', 'precios': 'Precio'},
                     trendline="ols", hover_data=['nombre', 'opiniones'])
    fig.update_layout(
        paper_bgcolor="black",
        plot_bgcolor="black",
        font_color="white",
        title_font_color="white"
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
            title_font_color="white"
        )
        return fig
