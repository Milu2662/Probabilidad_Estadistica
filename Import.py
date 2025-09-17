import pandas as pd
from io import StringIO

# Datos CSV emulados como string
data_csv = """Categoria,Producto,Venta
1,A,6
2,B,2
1,C,1
1,B,4
2,A,5
1,A,2
"""

# Crear DataFrame leyendo desde el string CSV
df = pd.read_csv(StringIO(data_csv))

# Extraer la columna 'Venta' como Serie
serie_ventas = df['Venta']

# Imprimir la Serie
print(serie_ventas)
