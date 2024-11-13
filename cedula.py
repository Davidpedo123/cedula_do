import numpy as np
import re
from concurrent.futures import ThreadPoolExecutor
import gc

def ajustar_cedula(cedula):
    """
    Ajusta una cédula eliminando guiones, reemplazando 'O' o 'o' por '0', y asegurando que tenga 11 caracteres.
    Formatea la cédula como 'xxx-xxxxxxx-x'.
    """
    cedula_sin_guion = re.sub(r'[Oo]', '0', str(cedula))  # Reemplazar 'O' y 'o' por '0'
    cedula_sin_guion = re.sub(r'[^0-9]', '', cedula_sin_guion)  # Eliminar cualquier carácter no numérico

    longitud = len(cedula_sin_guion)
    diferencia = 11 - longitud  # Calcular diferencia y aplicar relleno
    cedula_sin_guion = '0' * max(diferencia, 0) + cedula_sin_guion  # Rellenar con ceros a la izquierda

    return f"{cedula_sin_guion[:3]}-{cedula_sin_guion[3:10]}-{cedula_sin_guion[-1]}"

#def ajustar_cedulas_numpy(cedulas):
    """
    Ajusta una lista de cédulas utilizando operaciones vectorizadas con NumPy y expresiones regulares.
    
    cedulas = np.array(cedulas)

    cedulas = np.char.replace(cedulas, 'O', '0')
    cedulas = np.char.replace(cedulas, 'o', '0')

    cedulas = np.char.replace(cedulas, "-", "")  # Eliminar guiones

    cedulas = np.char.zfill(cedulas, 11)  # Rellenar con ceros a la izquierda si es necesario

    # Ajustar cédulas en el formato 'xxx-xxxxxxx-x'
    cedulas_formateadas = np.char.add(cedulas[:,:3], '-')  # Primer corte para los primeros tres números
    cedulas_formateadas = np.char.add(cedulas_formateadas, cedulas[:, 3:10])  # Añadir los siguientes 7
    cedulas_formateadas = np.char.add(cedulas_formateadas, '-' + cedulas[:, 10:11])  # El último número después del guion

    return cedulas_formateadas.tolist()
    """
def ajustar_cedulas_con_hilos(cedulas):
    """
    Ajusta las cédulas utilizando ThreadPoolExecutor para paralelizar el trabajo.
    """
    with ThreadPoolExecutor() as executor:
        resultados = list(executor.map(ajustar_cedula, cedulas))
    
    # Llamar al recolector de basura de Python para liberar la memoria
    gc.collect()

    return resultados

# Ejemplo de uso:
if __name__ == "__main__":
    cedulas = ['123-O4567890', '234-56789012', 'O345-6789012']
    cedulas_ajustadas = ajustar_cedulas_con_hilos(cedulas)
    print(cedulas_ajustadas)
