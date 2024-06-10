import pandas as pd


# Eliminar las comas de los valores en la columna "precios"
def eliminar_comas_precios(dataframe):
    dataframe["precios"] = dataframe["precios"].str.replace(",", "")

    return dataframe

# Convertir la columna "precios" a tipo numérico
def ordenar_por_precios(dataframe):
    dataframe["precios"] = pd.to_numeric(dataframe["precios"])

    # Ordenar el DataFrame por la columna "precios", de mayor a menor
    dataframe_ordenado = dataframe.sort_values(by="precios", ascending=False)

    return dataframe_ordenado


 # Eliminar las comas de los valores en la columna "precios" y convertirlos a números
def ordenar_por_preciosmercadolibre(dataframe):

    dataframe["precios"] = dataframe["precios"].str.replace(",", "").str.replace("$", "").astype(float)

    # Ordenar el DataFrame por la columna "precios", de mayor a menor
    dataframe_ordenado = dataframe.sort_values(by="precios", ascending=False)

    return dataframe_ordenado


def agregar_columna_amazon_desde_csv(ruta_csv):
    df = pd.read_csv(ruta_csv)

    # Agregar la columna 'Amazon' con el valor 'Sí' para cada fila
    df['paguina web'] = 'MERCADO LIBRE'
    return df

def concatenar_csv(archivo1, archivo2):
    df1 = pd.read_csv(archivo1)
    df2 = pd.read_csv(archivo2)

    # Concatenar los DataFrames uno encima del otro (por filas)
    df_concatenado = pd.concat([df1, df2])

    return df_concatenado


def limpiar_calificaciones_csv(file_path):
    data = pd.read_csv(file_path)

    # Limpiar la columna "calificasion"
    data['calificasion'] = data['calificasion'].str.extract(r'(\d+\.\d+)')
    data['calificasion'] = pd.to_numeric(data['calificasion'])

    return data


def convertir_opiniones_a_numerico(data):
    # Convertir la columna 'opiniones' a tipo numérico
    data['opiniones'] = pd.to_numeric(data['opiniones'],
                                      errors='coerce')  # 'coerce' convierte valores no numéricos a NaN

    return data


def contar_opiniones_por_genero_en_csv(ruta_archivo):
    dataframe = pd.read_csv(ruta_archivo)

    # Agrupar por genero y sumar las opiniones
    total_opiniones_por_genero = dataframe.groupby('paguina web')['opiniones'].sum().reset_index()
    return total_opiniones_por_genero


def eliminar_datos_nulos_csv(archivo_entrada, archivo_salida):
    dataframe = pd.read_csv(archivo_entrada)

    # Eliminar filas con valores nulos
    dataframe_limpio = dataframe.dropna()

    # Guardar el DataFrame limpio como un nuevo archivo CSV
    dataframe_limpio.to_csv(archivo_salida, index=False)


def eliminar_duplicados_csv(archivo_entrada, archivo_salida):
    dataframe = pd.read_csv(archivo_entrada)

    # Eliminar filas duplicadas
    dataframe_sin_duplicados = dataframe.drop_duplicates()

    # Guardar el DataFrame sin duplicados como un nuevo archivo CSV
    dataframe_sin_duplicados.to_csv(archivo_salida, index=False)
    print("Se han eliminado los duplicados y se ha guardado el archivo limpio como:", archivo_salida)


def tipos_de_datos_csv(archivo_csv):
    data = pd.read_csv(archivo_csv)
    tipos = {}
    for columna in data.columns:
        tipos[columna] = data[columna].dtype
    return tipos


if __name__ == "__main__":
    #ruta_archivo = "dataset/concatenado.csv"
    #contar=contar_opiniones_por_genero_en_csv(ruta_archivo)
    #print(contar)
    #--------------------------------------------------------------------#



    #data = pd.read_csv("dataset/amazon_12.csv")#=================#4 #Elimina las comas de la columna precios#
    #df_limpiado = eliminar_comas_precios(data)#==================# #Sirve unicamente para el scrappping de amazon#
    #df = pd.DataFrame(df_limpiado)
    #df.to_csv("dataset/amazon_12.csv", index=False)



    #data = pd.read_csv("dataset/amazon_12.csv")#==============#5 #Ordena los precios de mayor a menor del scrapping amazon#
    #df_ordenado = ordenar_por_precios(data)
    #df = pd.DataFrame(df_ordenado)
    #df.to_csv("dataset/amazon_12.csv", index=False)

    #df = pd.read_csv("dataset/merdolibreprueba.csv")#==========# #Ordena los precios de mayor a menor  del scrapping de mercado libre#
    #df_ordenado=ordenar_por_preciosmercadolibre(df)
    #df = pd.DataFrame(df_ordenado)
    #df.to_csv("dataset/mercadolibreelbueno.csv", index=False)





    #ruta_archivo_csv = "dataset/amazon_12.csv"
    #Agregar la columna 'Amazon' al DataFrame desde el archivo CSV
    #df_con_amazon = agregar_columna_amazon_desde_csv(ruta_archivo_csv)#================#3
    #print(df_con_amazon)#===========# #Crea una columna nueva en el scrapping donde se desea. Se agrega en la ultima columna#
    #df = pd.DataFrame(df_con_amazon)
    #df.to_csv("dataset/amazon_12.csv", index=False)

    #ruta_archivo_csv = "dataset/mercadolibreelbueno.csv"#Crea una columna nueva en el scrapping donde se desea. Se agrega en la ultima columna#
    #Agregar la columna 'Amazon' al DataFrame desde el archivo CSV
    #df_con_amazon = agregar_columna_amazon_desde_csv(ruta_archivo_csv)
    #print(df_con_amazon)
    #df = pd.DataFrame(df_con_amazon)
    #df.to_csv("dataset/mercadolibreelbueno.csv", index=False)

    #df_concatenado = concatenar_csv("dataset/amazon_12.csv", "dataset/mercadolibreelbueno.csv")
    #print(df_concatenado)# Une dos csv en uno solo #
    #df = pd.DataFrame(df_concatenado)
    #df.to_csv("dataset/concatenado.csv", index=False)



    #ruta_archivo = "dataset/amazon_12.csv"
     #Llamar a la función para limpiar la columna 'calificasion' del archivo CSV#=======================#2
    #datos_limpiados = limpiar_calificaciones_csv(ruta_archivo)
     #Ver los datos limpios
    #print(datos_limpiados)
    #datos_limpiados.to_csv("dataset/amazon_12.csv", index=False)

    #ruta_archivo = "dataset/mercadolibreelbueno.csv"
    # Llamar a la función para limpiar la columna 'calificasion' del archivo CSV
    #datos_limpiados = limpiar_calificaciones_csv(ruta_archivo)
    ## Ver los datos limpios
    #print(datos_limpiados)
    #datos_limpiados.to_csv("dataset/mercadolibreelbueno.csv", index=False)




    #ruta_archivo = "dataset/amazon_12.csv"
    #data = pd.read_csv(ruta_archivo)
    #data = convertir_opiniones_a_numerico(data)#============#1
    #data.to_csv("dataset/amazon_12.csv", index=False)

    #ruta_archivo = "dataset/mercadolibreelbueno.csv"
    #data = pd.read_csv(ruta_archivo)
    #data = convertir_opiniones_a_numerico(data)
    #data.to_csv("dataset/mercadolibreelbueno.csv", index=False)





    #eliminar_datos_nulos_csv("dataset/amazon_12.csv", "dataset/amazon_12.csv")#=========#6# elimina datos nulos de scrapping que desees#
    #eliminar_datos_nulos_csv("dataset/mercadolibreelbueno.csv", "dataset/mercadolibreelbueno.csv")elimina datos nulos de scrapping que desees#
    #eliminar_duplicados_csv("dataset/amazonelbueno.csv", "dataset/amazonelbueno.csv")#elimina datos dupicados del scrapping que desees
    #eliminar_duplicados_csv("dataset/mercadolibreelbueno.csv", "dataset/mercadolibreelbueno.csv")#elimina datos dupicados del scrapping que desees

    #tipos_de_datos = tipos_de_datos_csv("dataset/concatenado0.csv")# muestra que tipos de datos se tiene en el csv
    #print(tipos_de_datos)

