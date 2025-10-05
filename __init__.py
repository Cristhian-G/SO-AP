"""
Proyecto SO-AP - Simulador de algoritmos de planificación de procesos
"""

# Importar las clases principales para facilitar el acceso

__version__ = "1.0.0"
__author__ = "Tu Nombre"
__description__ = "Simulador de algoritmo FCFS (First-Come, First-Served)"
__license__ = "MIT"

# Metadata del proyecto
PROJECT_NAME = "SO-AP"
PROJECT_DESCRIPTION = "Simulador de algoritmos de planificación de procesos"

# Lista de módulos que se importan con "from app import *"
__all__ = ['Proceso', 'Pila']

try:
    from app.proceso import Proceso
    from app.pila import Pila
except ImportError as e:
    pass
