import pandas as pd

# Crear DataFrame con las categorías y cantidades
datos = {
    'Evento': ['M', 'I', 'M_I', 'Ninguna'],
    'Cantidad': [12, 36, 6, 18]
}
df = pd.DataFrame(datos)

total = 60

# Calcular probabilidades individuales
p_M = df.loc[df['Evento']=='M', 'Cantidad'].values[0] / total
p_I = df.loc[df['Evento']=='I', 'Cantidad'].values[0] / total
p_M_I = df.loc[df['Evento']=='M_I', 'Cantidad'].values[0] / total

# Calcular probabilidades condicionales
p_M_dado_I = p_M_I / p_I
p_I_dado_M = p_M_I / p_M

print(f"P(M | I) = {p_M_dado_I:.3f}")
print(f"P(I | M) = {p_I_dado_M:.3f}")
