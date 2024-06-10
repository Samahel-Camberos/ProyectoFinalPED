import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, dash_table, callback, Input, Output


def filtros():
    tarjeta_filtros = dbc.Card(
        dbc.CardBody([
            html.Div([
                dbc.Label("Empresa para el primer conjunto de datos:"),
                dcc.Dropdown(
                    id="ddlCompany",
                    options=[
                        {"label": "Amazon", "value": "Amazon"},
                        {"label": "Mercado Libre", "value": "Mercado libre"}
                    ],
                    value="Amazon"
                )
            ])
        ])
    )
    return tarjeta_filtros


def dashboard(data1:pd.DataFrame):
    # Sumar las opiniones por página web
    total_opiniones_por_pagina = data1.groupby('paguina web')['opiniones'].sum().reset_index()

    # Ordenar de manera ascendente por el total de opiniones
    total_opiniones_por_pagina = total_opiniones_por_pagina.sort_values(by='opiniones', ascending=True)

    # Crear el gráfico de barras
    fig_line1 = px.bar(total_opiniones_por_pagina, x="paguina web", y="opiniones",
                       title="Total de Opiniones por Página Web (Ascendente)",
                       color="paguina web", barmode="group")
    body = html.Div([
        html.H2("Comparación de Productos", style={"textAlign": "center", "color": "blue"}),
        html.P("Comparación de calificaciones y precios de productos entre dos conjuntos de datos."),
        html.Hr(),
        dbc.Row([
            dbc.Col(filtros(), width=3),
            dbc.Col([
                dbc.Row([
                    dbc.Col(dash_table.DataTable(data=data1.to_dict("records"), page_size=10)),
                    dbc.Col(dcc.Graph(id="figLine1", figure=fig_line1)),
                    dbc.Col(dcc.Graph(id="figLine2")),
                ]),
                dbc.Row([
                    dbc.Col(dcc.Graph(id="figBarCombined")),
                    dbc.Col(dcc.Graph(id="figCalificaciones"))
                ]),
            ], width=9)
        ])
    ])
    return body


@callback(
    Output(component_id="figLine2", component_property="figure"),
    Output(component_id="figBarCombined", component_property="figure"),
    Input(component_id="ddlCompany", component_property="value")
)
def evento(company):
    # Carga de datos desde el archivo CSV
    data = pd.read_csv("dataset/concatenado.csv")
    # Filtrado de datos según la empresa seleccionada
    if company == "AMAZON":
        data_filtered = data[data['paguina web'].str.lower() == 'amazone']
    elif company == "MERCADO LIBRE":
        data_filtered = data[data['paguina web'].str.lower() == 'mercado libre']
    else:
        data_filtered = data  # Si no se selecciona ninguna empresa, se muestran todos los datos

    # Eliminar filas con valores nulos en las columnas 'genero' y 'precios'
    data_filtered = data_filtered.dropna(subset=['genero', 'precios'])

    # Conteo de género por página web
    conteo_genero_pagina = data_filtered.groupby(['paguina web', 'genero']).size().reset_index(name='count')

    # Crear el gráfico de barras para las ventas por género
    fig_line2 = px.bar(data_filtered, x="genero", y="precios", title=f"Ventas {company}")

    # Crear el gráfico de barras combinadas para la cantidad de productos por género y página web
    fig_bar_combined = px.bar(conteo_genero_pagina, x="count", y="paguina web", color="genero", barmode="group",
                              title="Cantidad de Productos por Género y Página Web",
                              orientation='h',  # barras horizontales
                              category_orders={"paguina web": ["mercado libre", "amazone"]})  # orden de las páginas web

    return fig_line2, fig_bar_combined


@callback(
    Output(component_id="figCalificaciones", component_property="figure"),
    Input(component_id="ddlCompany", component_property="value")
)
def analisis_calificaciones(empresa):
    # Carga de datos desde el archivo CSV
    data = pd.read_csv("dataset/concatenado.csv")
    # Filtrado de datos según la empresa seleccionada
    if empresa == "AMAZON":
        data_filtered = data[data['paguina web'].str.lower() == 'amazone']
    elif empresa == "MERCADO LIBRE":
        data_filtered = data[data['paguina web'].str.lower() == 'mercado libre']
    else:
        data_filtered = data  # Si no se selecciona ninguna empresa, se muestran todos los datos

    # Imprimir los datos filtrados para verificar
    print("Datos filtrados:")
    print(data_filtered)
    print(data['paguina web'].unique())

    # Agrupar por empresa y calcular el promedio de calificaciones
    promedio_calificaciones = data_filtered.groupby('paguina web')['calificasion'].mean().reset_index()

    # Crear el gráfico de barras
    fig_calificaciones = px.bar(promedio_calificaciones, x='paguina web', y='calificasion',
                                 title="Promedio de Calificaciones por Empresa",
                                 color='paguina web', labels={'calificasion': 'Calificación Promedio'})

    return fig_calificaciones


if __name__ == "__main__":
    data1 = pd.read_csv("dataset/concatenado.csv")
    app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
    app.layout = dashboard(data1)
    app.run_server(debug=True)