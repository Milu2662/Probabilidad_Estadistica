import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

lmbda = 2          # tasa promedio (ejemplo: accidentes/hora)
k = np.arange(0, 8)
pmf = poisson.pmf(k, lmbda)

print("Tabla Poisson (k, P(X=k)):")
for i in range(len(k)):
    print(f"{k[i]:>2} {pmf[i]:.4f}")

plt.stem(k, pmf, 'b', markerfmt='bo', basefmt=" ", use_line_collection=True)
plt.xlabel("Número de sucesos")
plt.ylabel("P(X=k)")
plt.title("Distribución Poisson λ=2")
plt.grid(axis='y', alpha=0.75)
plt.show()
