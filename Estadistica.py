import pandas as pd

# Datos de ejemplo
datos = {
    'Estudiante': ['A', 'B', 'C', 'D', 'E'],
    'Nota': [3.5, 4.0, 2.8, 3.9, 3.2]
}
df = pd.DataFrame(datos)

# Calcular la media
media = df['Nota'].mean()
print(f"Media: {media}")

# Calcular la mediana
mediana = df['Nota'].median()
print(f"Mediana: {mediana}")

# Calcular la moda
moda = df['Nota'].mode()
print(f"Moda(s): {moda.values}")

# Calcular la desviación estándar
desviacion = df['Nota'].std()
print(f"Desviación estándar: {desviacion}")

# Calcular la varianza
varianza = df['Nota'].var()
print(f"Varianza: {varianza}")
