# Scraper de Títulos en Python.

import requests
from bs4 import BeautifulSoup

def normalizar_url(url):
    # Agrega http:// si la URL no tiene esquema.
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    return url

def obtener_html(url):
    # Descarga el HTML de la página.
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Lanza error si el código HTTP no es 200.
        return respuesta.text
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener la página: {e}")
        return None

def extraer_etiquetas(html, etiqueta):
    # Extrae texto de las etiquetas HTML solicitadas.
    sopa = BeautifulSoup(html, 'html.parser')
    elementos = sopa.find_all(etiqueta)
    resultados = [elem.get_text(strip=True) for elem in elementos]
    return resultados

def guardar_en_archivo(resultados, nombre_archivo="Títulos extraídos.txt"):
    # Guarda los resultados en un archivo de texto.
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        for linea in resultados:
            f.write(linea + "\n")
    print(f"Resultados guardados en {nombre_archivo}")

def main():
    print("Scraper de Títulos")
    url = input("Ingresa la URL: ").strip()
    etiqueta = input("Ingresa la etiqueta HTML que deseas extraer (ej. h1, h2, p): ").strip()

    url = normalizar_url(url)
    html = obtener_html(url)

    if html:
        resultados = extraer_etiquetas(html, etiqueta)

        if resultados:
            print(f"\nSe encontraron {len(resultados)} elementos <{etiqueta}>:\n")
            for i, texto in enumerate(resultados, 1):
                print(f"{i}. {texto}")
            opcion = input("\n¿Deseas guardar los resultados en un archivo? (s/n): ").lower()
            if opcion == 's':
                guardar_en_archivo(resultados)
        else:
            print(f"No se encontraron etiquetas <{etiqueta}> en la página.")
    else:
        print("No se pudo procesar la página.")

if __name__ == "__main__":
    main()