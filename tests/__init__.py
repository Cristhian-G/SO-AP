"""
Paquete tests - Contiene las pruebas unitarias del proyecto SO-AP
"""

# Este archivo permite que Python trate 'tests' como un paquete
# y facilita la importación de módulos desde otras carpetas

import sys
import os

# Agregar la carpeta app al path para poder importar los módulos
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app_path = os.path.join(project_root, 'app')

if app_path not in sys.path:
    sys.path.insert(0, app_path)

__version__ = "1.0.0"
__description__ = "Tests unitarios para el proyecto SO-AP"
