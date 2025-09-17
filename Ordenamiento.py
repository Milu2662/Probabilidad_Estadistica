import pandas as pd
import numpy as np

# Crear DataFrame de ejemplo
datos = {
    'Estudiante': ['A', 'B', 'C', 'D', 'E'],
    'Nota': [3.5, 4.0, 2.8, 3.9, 3.2]
}
df = pd.DataFrame(datos)

# Ordenar por la columna 'Nota' en orden descendente
df_ordenado = df.sort_values(by='Nota', ascending=False)
print("Datos ordenados por nota (descendente):")
print(df_ordenado)
