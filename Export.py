import pandas as pd

# Datos de ejemplo como diccionario
ventas = {
    'Categoria':[1,2,1,1,2,1],
    'Producto': ['A','B','C','B','A','A'],
    'Venta': [6,2,1,4,5,2]
}
# Crear el DataFrame
df = pd.DataFrame(Ventas)

#Imprimir el DataFrame
print(df)

#Exportar el DataFrame a un archivo Excel (.xlsx)
df.to_excel('ventas_exportadas.xlsx', index=True)