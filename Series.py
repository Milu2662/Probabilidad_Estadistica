import pandas as pd

# Datos de ejemplo como diccionario
ventas = {
    'Categoria':[1,2,1,1,2,1],
    'Producto': ['A','B','C','B','A','A'],
    'Venta': [6,2,1,4,5,2]
}
# Crear el DataFrame
df = pd.DataFrame(Ventas)

#Extraer la columna 'Venta' como Serie
serie_ventas = df['Venta']

#Imprimir la Serie
print(serie_ventas)