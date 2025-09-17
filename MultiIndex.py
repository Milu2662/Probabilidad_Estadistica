import pandas as pd

# Datos de ejemplo como diccionario para varias dimensiones
datos = {
    ('Tienda1', 'Dia1'): [6, 2, 1],
    ('Tienda1', 'Dia2'): [4, 5, 2],
    ('Tienda2', 'Dia1'): [3, 2, 1],
    ('Tienda2', 'Dia2'): [5, 6, 3],
}

productos = ['A', 'B', 'C']

# Crear DataFrame con MultiIndex en las columnas
df_panel = pd.DataFrame(datos, index=productos)

# Imprimir el DataFrame
print(df_panel)
