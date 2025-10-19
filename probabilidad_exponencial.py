import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

lmbda = 1/10      # media=10 minutos, lambda=0.1
x = np.linspace(0, 60, 200)
pdf = expon.pdf(x, scale=1/lmbda)

# Ejemplo: P(X > 15)
p_mas_15 = 1 - expon.cdf(15, scale=1/lmbda)
print(f'P(X > 15) = {p_mas_15:.4f}')
# Ejemplo: P(X < 5)
p_menos_5 = expon.cdf(5, scale=1/lmbda)
print(f'P(X < 5) = {p_menos_5:.4f}')

print("Tabla Exponencial (x, P(x)):")
for xi in range(0, 61, 10):
    print(f"{xi} {expon.pdf(xi, scale=1/lmbda):.4f}")

plt.plot(x, pdf, color='orange', label="PDF")
plt.fill_between(x, pdf, where=(x>15), color='red', alpha=0.3, label="X>15")
plt.xlabel("Tiempo")
plt.ylabel("Densidad de probabilidad")
plt.title("Distribución Exponencial λ=0.1 (media=10)")
plt.legend()
plt.grid(True)
plt.show()
