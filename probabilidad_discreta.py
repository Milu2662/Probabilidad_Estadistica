# Aplicación: Funciones de Probabilidad Conjunta (Discretas)
# Autora: Luisa Fernanda Velasco López
# Código: 20212020106
# ============================================

# Librerías utilizadas
import itertools

# --------------------------------------------------------
# EJERCICIO 1: Selección de estudiantes del salón
# --------------------------------------------------------
def ejercicio1():
    print("\n=== EJERCICIO 1: Distribución Conjunta Discreta ===")
    # Valores de la tabla según el PDF
    casos = {(0,0):3, (0,1):6, (0,2):1, (1,0):9, (1,1):6, (2,0):3}
    total = sum(casos.values())
    # Normalización
    fxy = {k: v/total for k,v in casos.items()}

    print("{:<10}{:<10}{:<10}".format("X","Y","P(X,Y)"))
    for (x,y),p in fxy.items():
        print("{:<10}{:<10}{:<10.3f}".format(x,y,p))

    print("\nComprobación de normalización: ΣP(X,Y) =", round(sum(fxy.values()),3))

# --------------------------------------------------------
# EJERCICIO 3: Ejemplo discreto generalizado
# --------------------------------------------------------
def ejercicio3():
    print("\n=== EJERCICIO 3: Cálculo de marginales y condicionales ===")
    matriz = {(0,0):0.1, (0,1):0.2, (1,0):0.3, (1,1):0.4}

    # Probabilidades marginales
    Px = {x: sum(p for (i,y),p in matriz.items() if i==x) for x in {i for i,_ in matriz}}
    Py = {y: sum(p for (x,j),p in matriz.items() if j==y) for y in {j for _,j in matriz}}

    print("\nMarginal en X:")
    for x,p in Px.items(): print(f"P(X={x}) = {p:.2f}")

    print("\nMarginal en Y:")
    for y,p in Py.items(): print(f"P(Y={y}) = {p:.2f}")

    print("\nProbabilidades condicionales P(X|Y):")
    for (x,y),p in matriz.items():
        print(f"P(X={x}|Y={y}) = {p/Py[y]:.2f}")

if __name__ == "__main__":
    ejercicio1()
    ejercicio3()
