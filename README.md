# Titles Scraper en Python

Scraper en **Python** diseñado para extraer texto de etiquetas HTML específicas (como `h1`, `h2`, `p`, entre otras) desde una URL. Incluye manejo de errores HTTP, normalización de URL y opción para guardar los resultados en un archivo de texto.

---

## Características principales

- Normaliza la URL agregando `http://` automáticamente si es necesario.
- Descarga y analiza el contenido HTML de la página.
- Extrae todas las etiquetas HTML específicadas (por ejemplo, `h1`, `h2`, `p`).
- Maneja errores de conexión y respuestas HTTP no exitosas.
- Permite guardar los resultados extraídos en un archivo de texto (`Títulos extraídos.txt`).
- Interfaz por consola fácil de usar e intuitiva.

---

## Estructura del proyecto

```
/ titles-scraper
├─ titles_scraper.py        # Script principal del scraper.
└─ README.md                # Documentación del proyecto.
```

---

## Requisitos

- Python **3.8** o superior.
- Paquetes necesarios:
  - `requests`.
  - `beautifulsoup4`.

Instala las dependencias con:

   ```bash
   pip install requests beautifulsoup4
   ```

---

## Ejecución

### En Linux o macOS

1. Abre una terminal en la carpeta del proyecto.
2. Ejecuta:

   ```bash
   python3 titles_scraper.py
   ```

### En Windows

1. Abre una terminal en la carpeta del proyecto.
2. Ejecuta:

   ```bash
   python titles_scraper.py
   ```

### Ejemplo de uso

```
Ingresa la URL: ejemplo.com
Ingresa la etiqueta HTML que deseas extraer (ej. h1, h2, p): h1
Se encontraron 2 elementos <h1>:
1. Bienvenido al sitio
2. Últimas noticias
¿Deseas guardar los resultados en un archivo? (s/n):
```

---

## Autor

Alan Aquino.
