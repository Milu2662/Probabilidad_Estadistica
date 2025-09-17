import pandas as pd
import numpy as np

# Crear DataFrame de ejemplo con datos y valores nulos
datos = {
    'Estudiante': ['A', 'B', 'C', 'D', 'E'],
    'Nota': [3.5, 4.0, np.nan, 3.9, 3.2],
    'Materia': ['Matemáticas', 'Inglés', 'Matemáticas', 'Inglés', 'Matemáticas']
}
df = pd.DataFrame(datos)

# Filtrar estudiantes con nota mayor a 3.5
df_filtrado = df[df['Nota'] > 3.5]
print("Filtrado de notas mayores a 3.5:")
print(df_filtrado)

# Seleccionar solo columnas 'Estudiante' y 'Nota'
df_seleccion = df.loc[:, ['Estudiante', 'Nota']]
print("\nSelección de columnas Estudiante y Nota:")
print(df_seleccion)
