# Aplicación: Funciones de Probabilidad Conjunta (Continuas)
# Autora: Luisa Fernanda Velasco López
# Código: 20212020106
# ============================================

import sympy as sp

# --------------------------------------------------------
# EJERCICIO 2: f(x,y) = (2/5)*(x+3y)
# --------------------------------------------------------
def ejercicio2():
    print("\n=== EJERCICIO 2: Función de Densidad Continua ===")
    x, y = sp.symbols('x y')
    f = (2/5)*(x + 3*y)

    # Verificación de que integra 1
    integral_total = sp.integrate(sp.integrate(f, (x,0,1)), (y,0,1))
    print("Integral total =", float(integral_total))

    # Región R: x de 0 hasta y/2, y de 0 a 1
    region = sp.integrate(sp.integrate(f, (x,0,y/2)), (y,0,1))
    print("Probabilidad en región R =", float(region))

# --------------------------------------------------------
# EJERCICIO 4: f(x,y) = k(x^2 + y^2)
# --------------------------------------------------------
def ejercicio4():
    print("\n=== EJERCICIO 4: Densidad con constante desconocida ===")
    x, y, k = sp.symbols('x y k')
    f = k*(x**2 + y**2)

    # Calcular k tal que la integral total = 1
    ecuacion = sp.integrate(sp.integrate(f, (x,0,1)), (y,0,1)) - 1
    k_val = sp.solve(ecuacion, k)[0]
    print("Constante k =", float(k_val))

    # Probabilidad sobre región R: 0<x<0.5, 0<y<0.5
    P_R = sp.integrate(sp.integrate(f.subs(k,k_val), (x,0,0.5)), (y,0,0.5))
    print("P(R) =", float(P_R))

if __name__ == "__main__":
    ejercicio2()
    ejercicio4()
