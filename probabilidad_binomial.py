import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

n, p = 8, 0.2
k = np.arange(0, n+1)
pmf = binom.pmf(k, n, p)

print("Tabla Binomial (k, P(X=k)):")
for i in range(len(k)):
    print(f"{k[i]:>2} {pmf[i]:.4f}")

plt.bar(k, pmf, color='skyblue', edgecolor='black')
plt.xlabel("Número de éxitos")
plt.ylabel("P(X=k)")
plt.title("Distribución Binomial n=8, p=0.2")
plt.grid(axis='y', alpha=0.75)
plt.show()
