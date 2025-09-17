import pandas as pd
import numpy as np

# Crear DataFrame con valores nulos
datos = {
    'Estudiante': ['A', 'B', 'C', 'D', 'E'],
    'Nota': [3.5, 4.0, np.nan, 3.9, np.nan]
}
df = pd.DataFrame(datos)

# Eliminar filas con valores nulos en 'Nota'
df_sin_nulos = df.dropna(subset=['Nota'])
print("Datos sin valores nulos:")
print(df_sin_nulos)

# Rellenar valores nulos con la media de la columna 'Nota'
media_nota = df['Nota'].mean()
df_relleno = df.fillna({'Nota': media_nota})
print("\nDatos con valores nulos rellenados con la media:")
print(df_relleno)
