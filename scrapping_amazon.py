import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup
import time

def boot_en_amazon1(cantidad, busqueda):
    # Configurar el servicio de GeckoDriver
    service = Service(GeckoDriverManager().install())

    # Configurar opciones del navegador
    options = webdriver.FirefoxOptions()
    options.add_argument("--window-size=1000,1200")

    # Crear instancia del navegador
    driver = webdriver.Firefox(service=service, options=options)

    # Abrir Amazon
    driver.get("https://www.amazon.com.mx/ref=nav_logo")

    # Esperar 10 segundos
    time.sleep(10)
    carga1 = driver.find_element(By.ID, "twotabsearchtextbox")
    time.sleep(10)
    carga1.send_keys(busqueda)
    time.sleep(10)
    boton1 = driver.find_element(By.ID, "nav-search-submit-button")
    boton1.click()

    # Esperar a que se carguen los resultados
    time.sleep(10)

    data = {"nombre": [],"genero":[],"calificasion":[], "opiniones": [],"precios": [],}

    for repeticion in range(cantidad):
        # Obtener el código fuente HTML de la página
        html = driver.page_source

        # Pasar el HTML a BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")

        # Encontrar todos los elementos que contienen los productos
        productos = soup.findAll("span", class_='a-size-base-plus a-color-base')
        tipo = soup.findAll("span", class_='a-text-normal')
        estrellas = soup.findAll("span", class_='a-icon-alt')
        opiniones = soup.findAll("span", class_='s-underline-text')
        precios = soup.findAll("span", class_='a-price-whole')


        # Recorrer los productos y guardar los datos en el diccionario
        for producto,tipos, estrella,opinion ,precio in zip(productos,tipo,estrellas,opiniones,precios):
            genero = extraer_nombre_y_genero(tipos)
            data["nombre"].append(producto.text)
            data["genero"].append(genero)
            data["calificasion"].append(estrella.text)
            data["opiniones"].append(opinion.text)
            data["precios"].append(precio.text)

        boton_siguiente = driver.find_element(By.CLASS_NAME, "s-pagination-next")
        time.sleep(10)
        boton_siguiente.click()
        time.sleep(10)

    # Crear un DataFrame a partir del diccionaerio
    df = pd.DataFrame(data)
    print(df)
    df.to_csv("dataset/amazon_12.csv", index=False)


    # Cerrar el navegador
    driver.quit()


def extraer_nombre_y_genero(tipo):
    # Analizar el HTML del producto para extraer el género
    genero = "masculino" if "hombre" in tipo.text.lower() else "femenino"#===================#
    return genero


def limpiar_y_convertir_precios(dataframe):
    # Eliminar las comas de los valores en la columna "precios"
    dataframe["precios"] = dataframe["precios"].str.replace(",", "")#=====================#

    # Convertir la columna "precios" a tipo entero
    dataframe["precios"] = dataframe["precios"].astype(int)

    return dataframe


if __name__ == "__main__":
    boot_en_amazon1(6, "calzado nike")
