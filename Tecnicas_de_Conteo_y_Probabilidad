"""
Técnicas de Conteo y Probabilidad - Aplicación Empresarial
Autor: Luisa Fernanda Velasco López
Código: 20212020106
Universidad Distrital Francisco José de Caldas
"""

import math
from itertools import permutations, combinations
import random
from typing import List, Tuple

class TecnicasConteo:
    """Clase para implementar técnicas de conteo"""
    
    @staticmethod
    def factorial(n: int) -> int:
        """Calcula el factorial de n"""
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos")
        return math.factorial(n)
    
    @staticmethod
    def permutacion(n: int, r: int) -> int:
        """
        Calcula P(n,r) = n!/(n-r)!
        n: total de elementos
        r: elementos a ordenar
        """
        if r > n:
            return 0
        return math.factorial(n) // math.factorial(n - r)
    
    @staticmethod
    def combinacion(n: int, r: int) -> int:
        """
        Calcula C(n,r) = n!/(r!(n-r)!)
        n: total de elementos
        r: elementos a seleccionar
        """
        if r > n:
            return 0
        return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

class Probabilidad:
    """Clase para cálculos de probabilidad"""
    
    @staticmethod
    def probabilidad_clasica(casos_favorables: int, casos_posibles: int) -> float:
        """Calcula probabilidad clásica"""
        if casos_posibles == 0:
            raise ValueError("El número de casos posibles no puede ser cero")
        return casos_favorables / casos_posibles
    
    @staticmethod
    def probabilidad_complemento(p: float) -> float:
        """Calcula P(A^c) = 1 - P(A)"""
        return 1 - p

class AplicacionEmpresarial:
    """Aplicación práctica: Optimización de rutas de distribución"""
    
    def __init__(self, num_clientes: int):
        self.num_clientes = num_clientes
        self.clientes = [f"Cliente_{i+1}" for i in range(num_clientes)]
    
    def calcular_rutas_posibles(self) -> int:
        """Calcula el número total de rutas posibles"""
        return TecnicasConteo.factorial(self.num_clientes)
    
    def calcular_rutas_con_restriccion(self, cliente_inicio: str, cliente_fin: str) -> int:
        """
        Calcula rutas que comienzan y terminan en clientes específicos
        """
        # Fijamos inicio y fin, permutamos los demás
        clientes_intermedios = self.num_clientes - 2
        return TecnicasConteo.factorial(clientes_intermedios)
    
    def generar_muestra_rutas(self, n_rutas: int) -> List[List[str]]:
        """Genera una muestra aleatoria de rutas"""
        rutas = []
        for _ in range(n_rutas):
            ruta = random.sample(self.clientes, self.num_clientes)
            rutas.append(ruta)
        return rutas

def ejemplo_1_seleccion_personal():
    """
    Ejemplo 1: Selección de comité
    10 candidatos (6 ingenieros, 4 administradores)
    Comité de 4 personas
    """
    print("=" * 60)
    print("EJEMPLO 1: SELECCIÓN DE PERSONAL")
    print("=" * 60)
    
    # Parte 1: Total de formas de seleccionar el comité
    total_candidatos = 10
    tamano_comite = 4
    
    total_comites = TecnicasConteo.combinacion(total_candidatos, tamano_comite)
    print(f"\n1. Formas de seleccionar el comité: {total_comites}")
    
    # Parte 2: Probabilidad de 2 ingenieros y 2 administradores
    ingenieros = 6
    administradores = 4
    
    formas_2ing_2adm = (TecnicasConteo.combinacion(ingenieros, 2) * 
                        TecnicasConteo.combinacion(administradores, 2))
    
    prob = Probabilidad.probabilidad_clasica(formas_2ing_2adm, total_comites)
    
    print(f"2. Formas de seleccionar 2 ing y 2 adm: {formas_2ing_2adm}")
    print(f"3. Probabilidad: {prob:.4f} ({prob*100:.2f}%)")

def ejemplo_2_control_calidad():
    """
    Ejemplo 2: Control de calidad
    100 unidades (95 buenas, 5 defectuosas)
    Muestra de 5 unidades
    """
    print("\n" + "=" * 60)
    print("EJEMPLO 2: CONTROL DE CALIDAD")
    print("=" * 60)
    
    total_unidades = 100
    unidades_buenas = 95
    unidades_defectuosas = 5
    tamano_muestra = 5
    
    # Total de formas de seleccionar la muestra
    total_muestras = TecnicasConteo.combinacion(total_unidades, tamano_muestra)
    
    # Probabilidad de 0 defectuosas
    formas_0_def = TecnicasConteo.combinacion(unidades_buenas, tamano_muestra)
    prob_0_def = Probabilidad.probabilidad_clasica(formas_0_def, total_muestras)
    
    print(f"\n1. Total de muestras posibles: {total_muestras}")
    print(f"2. Probabilidad de 0 defectuosas: {prob_0_def:.4f} ({prob_0_def*100:.2f}%)")
    
    # Probabilidad de 1 defectuosa
    formas_1_def = (TecnicasConteo.combinacion(unidades_defectuosas, 1) * 
                    TecnicasConteo.combinacion(unidades_buenas, 4))
    prob_1_def = Probabilidad.probabilidad_clasica(formas_1_def, total_muestras)
    
    print(f"3. Probabilidad de 1 defectuosa: {prob_1_def:.4f} ({prob_1_def*100:.2f}%)")

def aplicacion_empresarial():
    """
    Aplicación práctica: Optimización de rutas de distribución
    """
    print("\n" + "=" * 60)
    print("APLICACIÓN EMPRESARIAL: RUTAS DE DISTRIBUCIÓN")
    print("=" * 60)
    
    num_clientes = 6
    app = AplicacionEmpresarial(num_clientes)
    
    # Calcular total de rutas
    total_rutas = app.calcular_rutas_posibles()
    print(f"\n1. Total de rutas posibles visitando {num_clientes} clientes: {total_rutas}")
    
    # Rutas con restricciones
    rutas_restriccion = app.calcular_rutas_con_restriccion("Cliente_1", "Cliente_6")
    print(f"2. Rutas comenzando en Cliente_1 y terminando en Cliente_6: {rutas_restriccion}")
    
    # Generar muestra de rutas
    print("\n3. Muestra de 5 rutas aleatorias:")
    muestra_rutas = app.generar_muestra_rutas(5)
    for i, ruta in enumerate(muestra_rutas, 1):
        print(f"   Ruta {i}: {' → '.join(ruta)}")
    
    # Análisis probabilístico de demanda
    print("\n4. Análisis de probabilidad de demanda:")
    print("   - Probabilidad pedido grande: 60%")
    print("   - Probabilidad pedido mediano: 30%")
    print("   - Probabilidad pedido pequeño: 10%")
    
    # Simulación de escenarios
    prob_todos_grandes = 0.6 ** num_clientes
    print(f"\n5. Probabilidad de que todos los clientes hagan pedidos grandes:")
    print(f"   {prob_todos_grandes:.6f} ({prob_todos_grandes*100:.4f}%)")

def main():
    """Función principal que ejecuta todos los ejemplos"""
    print("\n" + "=" * 60)
    print("TÉCNICAS DE CONTEO Y PROBABILIDAD")
    print("Aplicaciones Empresariales")
    print("=" * 60)
    
    # Ejecutar ejemplos
    ejemplo_1_seleccion_personal()
    ejemplo_2_control_calidad()
    aplicacion_empresarial()
    
    print("\n" + "=" * 60)
    print("Repositorio: https://github.com/[tu-usuario]/probabilidad-tecnicas-conteo")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
