"""
Paquete app - Contiene las clases principales del proyecto SO-AP
"""

# Importar las clases principales para facilitar el acceso
from .proceso import Proceso
from .pila import Pila

# Información del paquete
__version__ = "1.0.0"
__author__ = "Tu Nombre"
__description__ = "Simulador de algoritmo FCFS para Sistemas Operativos"

# Lista de módulos que se importan con "from app import *"
__all__ = ['Proceso', 'Pila']
