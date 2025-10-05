
# 🖥️ SO-AP - Sistema Operativo: Algoritmos y Procesos

**Simulador interactivo del algoritmo de planificación FCFS (First-Come, First-Served)**

Un proyecto educativo para implementar y estudiar algoritmos de planificación de procesos en sistemas operativos, desarrollado en Python con interfaz de terminal.

## ✨ Características

- 🚀 **Simulación FCFS**: Implementación completa del algoritmo First-Come, First-Served
- 📊 **Métricas detalladas**: Cálculo de tiempo de espera y tiempo de retorno
- 🎨 **Interfaz colorida**: Terminal con colores y formato para mejor experiencia
- 🧪 **Tests unitarios**: Cobertura completa con pytest
- 📈 **Visualización paso a paso**: Muestra la ejecución del algoritmo en tiempo real

## 🏗️ Estructura del Proyecto

```
SO-AP/
├── .venv/              # Entorno virtual de Python
├── app/                # 📦 Código fuente principal
│   ├── __init__.py     # Configuración del paquete
│   ├── main.py         # 🚀 Punto de entrada con menús interactivos
│   ├── pila.py         # 📚 Implementación de Pila/Cola para FCFS
│   └── proceso.py      # ⚙️ Clase Proceso con estados y métricas
├── tests/              # 🧪 Tests unitarios completos
│   ├── __init__.py     # Configuración de tests
│   └── test_main.py    # Tests para Proceso y Pila
├── requirements.txt    # 📋 Dependencias del proyecto
├── .gitignore         # 🚫 Archivos a ignorar en Git
└── README.md          # 📖 Este archivo
```

## 🚀 Instalación y Configuración

### Prerrequisitos
- Python 3.8 o superior
- Git (opcional)

### Pasos de instalación

1. **Clona o descarga el proyecto:**
   ```bash
   git clone <tu-repositorio>
   cd SO-AP
   ```

2. **Activa el entorno virtual:**
   ```bash
   # En Windows (PowerShell)
   .\.venv\Scripts\Activate.ps1
   
   # En Windows (CMD)
   .venv\Scripts\activate.bat
   
   # En Linux/Mac
   source .venv/bin/activate
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Uso del Simulador

### Ejecutar la aplicación principal:
```bash
python app/main.py
```

### Opciones disponibles:
- **Menú interactivo**: Agrega procesos manualmente y simula
- **Demo automática**: Ejecuta una simulación con datos de ejemplo

### Ejemplo de uso:
```
=== SIMULADOR FCFS CON PILA ===
1. Agregar proceso
2. Mostrar procesos en cola
3. Ejecutar algoritmo FCFS
4. Reiniciar simulación
5. Salir

Seleccione una opción: 1
```

## 🔧 Desarrollo y Testing

### Estructura de clases principales:

#### **Clase Proceso** (`app/proceso.py`)
- ✅ Manejo de estados (nuevo, ejecutando, terminado)
- ✅ Cálculo automático de métricas
- ✅ Getters y setters para todos los atributos
- ✅ Método de ejecución paso a paso

#### **Clase Pila** (`app/pila.py`)
- ✅ Implementación de cola FCFS (ordenada por tiempo de llegada)
- ✅ Simulación completa del algoritmo FCFS
- ✅ Cálculo de métricas promedio
- ✅ Interfaz de visualización paso a paso

#### **Archivo Principal** (`app/main.py`)
- ✅ Menú interactivo con colores
- ✅ Validación de entrada de datos
- ✅ Demo con datos de ejemplo
- ✅ Manejo de errores robusto

### Ejecutar tests:
```bash
# Ejecutar todos los tests
python tests/test_main.py

# Con unittest (más detallado)
python -m unittest tests.test_main -v

# Con pytest (si está instalado)
python -m pytest tests/ -v
```

### Tests incluidos:
- ✅ **TestProceso**: Validación de la clase Proceso
- ✅ **TestPila**: Validación de operaciones de la Pila/Cola
- ✅ **TestIntegracionFCFS**: Tests de integración del algoritmo completo

## 📊 Ejemplo de Simulación

### Entrada de datos:
```
Proceso 1: PID=1, Nombre="Navegador", T.Llegada=0, T.Ejecución=5
Proceso 2: PID=2, Nombre="Editor", T.Llegada=1, T.Ejecución=3  
Proceso 3: PID=3, Nombre="Antivirus", T.Llegada=2, T.Ejecución=8
```

### Salida del simulador:
```
=== EJECUCIÓN ALGORITMO FCFS ===

Tiempo   Proceso         Estado       Tiempo Rest.
--------------------------------------------------
0        Navegador       ejecutando   5           
1        Navegador       ejecutando   4           
...
5        Navegador       terminado    0           
5        Editor          ejecutando   3           
...

=== MÉTRICAS DEL ALGORITMO ===
Proceso      T.Llegada    T.Ejecución  T.Finalización   T.Espera  
----------------------------------------------------------------------
Navegador    0            5            5                0         
Editor       1            3            8                4         
Antivirus    2            8            16               6         

Tiempo promedio de espera: 3.33
Tiempo promedio de retorno: 10.67
```

## 🎯 Algoritmo FCFS Implementado

El algoritmo **First-Come, First-Served** funciona de la siguiente manera:

1. **Llegada**: Los procesos se ordenan automáticamente por tiempo de llegada
2. **Ejecución**: El primer proceso en llegar se ejecuta hasta completarse
3. **No apropiativo**: Una vez que un proceso inicia, se ejecuta hasta terminar
4. **Cola FIFO**: Los procesos posteriores esperan en orden de llegada

### Métricas calculadas:
- **Tiempo de finalización**: Cuándo termina cada proceso
- **Tiempo de espera**: Tiempo que cada proceso espera antes de ejecutarse
- **Tiempo de retorno**: Tiempo total desde llegada hasta finalización

## 👨‍💻 Autorez

- **Cristhian German Ramirez Ruiz**
- **Irene Perez**
- **Alan Iñiguez Muños**
- **Cristopher Barajas Salvador**

---

⭐ **¡Múchas Gracias por su tiempo!** ⭐