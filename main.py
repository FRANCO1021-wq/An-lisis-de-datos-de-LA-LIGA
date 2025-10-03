# main.py
import pandas as pd

# Paso 1: Cargar los datos
laliga = pd.read_csv("laliga_2024_2025.csv")

# Paso 2: Mostrar forma del dataset (filas, columnas)
print("Tamaño del dataset:", laliga.shape)

# Paso 3: Ver los primeros 10 partidos
print("\nPrimeros 10 partidos:")
print(laliga.head(10))

# Goles totales por jornada
laliga["TotalGoles"] = laliga["FTHG"] + laliga["FTAG"]

print("\nPromedio de goles por partido:", laliga["TotalGoles"].mean())

# Partidos ganados por equipo local
local_ganados = laliga[laliga["FTR"] == "H"].shape[0]
print("Partidos ganados por locales:", local_ganados)

# Empates
empates = laliga[laliga["FTR"] == "D"].shape[0]
print("Empates:", empates)

# Partidos ganados por visitantes
visita_ganados = laliga[laliga["FTR"] == "A"].shape[0]
print("Partidos ganados por visitantes:", visita_ganados)

import matplotlib.pyplot as plt

# Histograma de goles totales por partido
plt.hist(laliga["TotalGoles"], bins=6, color='skyblue', edgecolor='black')
plt.title("Distribución de goles por partido")
plt.xlabel("Goles totales")
plt.ylabel("Frecuencia")
plt.grid(True)
plt.show()
