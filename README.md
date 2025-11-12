# LaLiga Insights Pro

## Integrantes
- Bayron Franco
- Andres Felipe Mambuscay
- Andres Fonseca

## Descripción
Nuestro proyecto de análisis de datos de LaLiga tiene como objetivo explorar y analizar estadísticas de equipos y jugadores en la liga española de fútbol. Se centra en evaluar el rendimiento de los equipos (goles, victorias, derrotas) y de jugadores (goles, asistencias) utilizando técnicas estadísticas y modelos predictivos en Python.

## Objetivos

### Objetivo general
Analizar el rendimiento de los equipos y jugadores de LaLiga mediante el uso de Python, aplicando técnicas estadísticas y modelos predictivos que permitan obtener información relevante sobre goles, victorias, derrotas y asistencias.

### Objetivos específicos
1. Recolectar datos de equipos y jugadores de LaLiga en un formato adecuado para su análisis.
2. Comparar el rendimiento de los equipos a partir de métricas clave como goles, victorias y derrotas.
3. Generar visualizaciones que faciliten la interpretación de los datos y los hallazgos del análisis.

## Requisitos
Se implementará como programa en Python, un lenguaje utilizado para este tipo de tareas por su facilidad y por las herramientas disponibles.  
Se usará principalmente:
- `pandas` para leer los datos de partidos y analizarlos como tablas.
- `matplotlib` y `seaborn` para generar gráficos que faciliten la comprensión de la información.

## Desarrollo

### Explicación paso a paso
1. **Definición del objetivo:** Crear un programa en Python para recolectar datos de equipos y jugadores de LaLiga 2024/25.  
2. **Selección de herramientas:** Python, `pandas`, `requests`, `BeautifulSoup`, `os`.  
3. **Obtención de datos:** Se identificaron las URLs de Transfermarkt para posiciones y goleadores.  
4. **Extracción y limpieza:** Se recorren las tablas HTML, se extraen las columnas necesarias y se convierten a DataFrame.  
5. **Generación de reportes:** Se guardan los CSV y se muestran tablas en consola.

### Fragmentos de código relevantes

```python
# Función para obtener tabla de posiciones
def obtener_tabla_posiciones():
    url = 'https://www.transfermarkt.com/laliga/tabelle/wettbewerb/ES1/saison_id/2024'
    headers = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        print(f'Error al conectar ({res.status_code}).')
        return pd.DataFrame()

    soup = BeautifulSoup(res.text, 'html.parser')
    tabla = soup.find('table', {'class': 'items'})
    equipos, partidos, puntos = [], [], []
    filas = tabla.find_all('tr', {'class': ['odd', 'even']})

    for fila in filas:
        columnas = fila.find_all('td')
        if len(columnas) >= 10:
            equipos.append(columnas[1].get_text(strip=True))
            partidos.append(columnas[2].get_text(strip=True))
            puntos.append(columnas[9].get_text(strip=True))

    df = pd.DataFrame({
        'Pos': range(1, len(equipos)+1),
        'Equipo': equipos,
        'PJ': partidos,
        'Puntos': puntos
    })
    return df
```
## Conclusiones

- Las visualizaciones facilitan la comprensión de patrones de rendimiento.  
- El proyecto combina programación, estadística y fútbol para un análisis profesional de LaLiga.  
- El uso de scraping y pandas permite automatizar la recolección y análisis de datos de manera eficiente.  
- Los menús interactivos mejoran la experiencia del usuario al explorar la información.  
- La generación de archivos CSV permite conservar registros históricos y facilitar su uso en otros análisis.  
- Se identificaron dificultades comunes en scraping, lo que refuerza la importancia de manejo de errores y validación de datos.  
- El proyecto sirve como base para incorporar futuras mejoras, como visualizaciones avanzadas y modelos predictivos.  
- La combinación de datos reales con análisis estadístico ofrece insights útiles para equipos, jugadores y aficionados.  

## Bibliografía / Recursos

- [Python Documentation](https://docs.python.org/3/)  
- [Pandas Documentation](https://pandas.pydata.org/docs/)  
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)  
- [Requests Documentation](https://docs.python-requests.org/)  
- [Transfermarkt](https://www.transfermarkt.com/)  
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)  
- [Seaborn Documentation](https://seaborn.pydata.org/)  
- [Tutorial scraping con Python en Real Python](https://realpython.com/beautiful-soup-web-scraper-python/)  
- [Kaggle – Soccer Data Analysis](https://www.kaggle.com/)  
- Artículos sobre análisis estadístico en fútbol

