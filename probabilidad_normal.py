import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mu, sigma = 15, 3   # media y desviación estándar (ejemplo: tiempo de consulta)
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 200)
pdf = norm.pdf(x, mu, sigma)

# Ejemplo: P(12 < X < 18)
p_12_18 = norm.cdf(18, mu, sigma) - norm.cdf(12, mu, sigma)
print(f'P(12 < X < 18) = {p_12_18:.4f}')

print("Tabla Normal (x, P(x)):")
for xi, pi in zip(np.arange(10,21,1), norm.pdf(np.arange(10,21,1), mu, sigma)):
    print(f"{xi} {pi:.4f}")

plt.plot(x, pdf, label="PDF")
plt.fill_between(x, pdf, where=((x>=12)&(x<=18)), color='skyblue', alpha=0.5, label="12 < x < 18")
plt.xlabel("Valor")
plt.ylabel("Densidad de probabilidad")
plt.title("Distribución Normal μ=15, σ=3")
plt.legend()
plt.grid(True)
plt.show()
