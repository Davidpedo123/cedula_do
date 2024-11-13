import time
import pytest
from .main import ajustar_cedula, ajustar_cedulas_con_hilos, ajustar_cedulas_numpy

# Función para medir el tiempo de ejecución
def medir_tiempo(func, *args):
    inicio = time.time()
    func(*args)
    fin = time.time()
    return fin - inicio

# Generador de cédulas de prueba
def generar_cedulas(cantidad):
    return [f"402-33{str(i).zfill(6)}-3" for i in range(cantidad)]

# Prueba de rendimiento con diferentes cantidades de cédulas
@pytest.mark.parametrize("cantidad_cedulas", [100, 1000, 10000, 100000])
def test_rendimiento_ajustar_cedula(cantidad_cedulas):
    print(f"Probando con {cantidad_cedulas} cédulas...")
    cedulas = generar_cedulas(cantidad_cedulas)
    
    # Medir el tiempo de ejecución de la función ajustar_cedula
    tiempo = medir_tiempo(ajustar_cedulas_con_hilos, cedulas)
    print(f"Tiempo para {cantidad_cedulas} cédulas con hilos: {tiempo:.4f} segundos")
    
    tiempo_numpy = medir_tiempo(ajustar_cedulas_numpy, cedulas)
    print(f"Tiempo para {cantidad_cedulas} cédulas con NumPy: {tiempo_numpy:.4f} segundos")
