"""
Este script se encarga de recopilar información sobre tenis Nike disponibles en la página
 web de Amazon. Utiliza técnicas de web scraping para extraer datos relevantes como el nombre
  del producto, precio, calificaciones, número de opiniones y URL del producto.
  Los datos extraídos se guardan en un archivo CSV para su posterior análisis.

"""
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
    service = Service(ChromeDriverManager().install())
    #service = Service(GeckoDriverManager().install())

    # Configurar opciones del navegador
    options = webdriver.ChromeOptions()
    #options = webdriver.FirefoxOptions()
    options.add_argument("--window-size=1000,1200")

    # Crear instancia del navegador
    driver = webdriver.Chrome(service=service, options=options)
    #driver = webdriver.Firefox(service=service, options=options)

    # Abrir Amazon
    driver.get("https://www.amazon.com.mx/ref=nav_logo")