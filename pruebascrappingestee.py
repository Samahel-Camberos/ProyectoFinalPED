import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def boot_en_merado_libre(busqueda, cantidad):
    # Configurar el servicio de GeckoDriver
    service = Service(GeckoDriverManager().install())

    # Configurar opciones del navegador
    options = webdriver.FirefoxOptions()
    options.add_argument("--window-size=1000,1200")

    # Crear instancia del navegador
    driver = webdriver.Firefox(service=service, options=options)

    # Abrir Mercado Libre
    driver.get("https://www.mercadolibre.com.mx/")

    # Buscar el campo de búsqueda y enviar la palabra clave
    campo_busqueda = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "cb1-edit"))
    )
    campo_busqueda.send_keys(busqueda)

    # Hacer clic en el botón de búsqueda
    boton_busqueda = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "nav-icon-search"))
    )
    boton_busqueda.click()

    data = {"nombre": [], "genero": [],"calificasion":[],"opiniones":[],"precios":[]}

    for _ in range(cantidad):
        # Esperar a que los resultados se carguen completamente
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ui-search-item__title"))
        )

        # Obtener el código fuente HTML de la página
        html = driver.page_source

        # Pasar el HTML a BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")

        # Encontrar todos los elementos que contienen los productos
        productos = soup.find_all('h2', class_='ui-search-item__title')
        calificasion = soup.findAll('span', class_='andes-visually-hidden')
        precio = soup.findAll('span', class_='andes-money-amount')


        for producto , calificasiones, precios in zip(productos, calificasion, precio):
            # Extraer nombre y género del producto
            nombre, genero = extraer_nombre_y_genero(producto)
            califi, opinion = extraer_calificasion_y_opiniones(calificasiones)
            data["nombre"].append(' '.join(nombre))  # Convertir la lista de palabras en una cadena de texto
            data["genero"].append(genero)
            data["calificasion"].append(' '.join(califi))
            data["opiniones"].append(' '.join(opinion))
            data["precios"].append(precios.text)


        # Buscar y hacer clic en el botón "Siguiente"
        try:
            boton_siguiente = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "andes-pagination__button andes-pagination__button--next"))
            )
            driver.execute_script("arguments[0].scrollIntoView();", boton_siguiente)
            boton_siguiente.click()
        except Exception as e:
            print(f"No se pudo hacer clic en el botón 'Siguiente': {e}")

    # Cerrar el navegador
    driver.quit()

    # Convertir los datos a un DataFrame de pandas y guardarlos en un archivo CSV
    df = pd.DataFrame(data)
    print(df)
    df.to_csv("dataset/merdolibreprueba.csv", index=False)





def extraer_nombre_y_genero(producto):
    # Extraer el nombre del producto
    nombre = producto.text.split(" ")[0:1]

    # Analizar el HTML del producto para extraer el género
    genero = "masculino" if "hombre" in producto.text.lower() else "femenino"

    return nombre, genero


def extraer_calificasion_y_opiniones(calificasiones):
    # Extraer el nombre del producto
    califi = calificasiones.text.split(" ")[0:2]
    opinion = calificasiones.text.split(" ")[4:5]
    return califi, opinion


if __name__ == "__main__":
    busqueda = "calzado nike"
    cantidad = 6
    boot_en_merado_libre(busqueda, cantidad)