from pila import Pila
from proceso import Proceso
from time import sleep
import os

def menu_principal():
    """Menú interactivo usando la Pila para FCFS"""
    pila_fcfs = Pila()
    
    while True:
        limpiar_pantalla()
        mostrar_banner()
        print(texto_negritas(texto_color("MENÚ PRINCIPAL", "Azul")))
        print(texto_color("1. Agregar proceso", "cyan"))
        print(texto_color("2. Mostrar procesos en cola", "cyan"))
        print(texto_color("3. Ejecutar FCFS", "verde"))
        print(texto_color("4. Reiniciar simulación", "amarillo"))
        print(texto_color("5. Salir", "rojo"))

        opcion = input(texto_negritas(texto_color("Seleccione una opción: ", "azul"))).strip() 

        if opcion == "1":
            try:
                pid = int(input(texto_negritas(texto_color("PID del proceso: ", "cyan"))))
                nombre = input(texto_negritas(texto_color("Nombre del proceso: ", "cyan")))
                tiempo_llegada = int(input(texto_negritas(texto_color("Tiempo de llegada: ", "cyan"))))
                tiempo_ejecucion = int(input(texto_negritas(texto_color("Tiempo de ejecución: ", "cyan"))))

                proceso = Proceso(pid, nombre, tiempo_llegada, tiempo_ejecucion)
                pila_fcfs.apilar(proceso)
                print(texto_negritas(texto_color(f"✅ Proceso {nombre} agregado a la cola","verde")))
                
            except ValueError:
                print(texto_negritas(texto_color("❌ Entrada inválida, intente de nuevo", "rojo")))
        
        elif opcion == "2":
            pila_fcfs.mostrar_cola()
        
        elif opcion == "3":
            if not pila_fcfs.esta_vacia():
                pila_fcfs.ejecutar_fcfs()
            else:
                print(texto_negritas(texto_color("❌ No hay procesos en la cola para ejecutar")))
        
        elif opcion == "4":
            pila_fcfs.reiniciar()
            print(texto_negritas(texto_color("🔄 Simulación reiniciada","verde")))
        
        elif opcion == "5":
            limpiar_pantalla()
            print(texto_negritas(texto_color("¡Hasta luego! 👋", "verde")))
            sleep(2)
            break
        
        else:
            print(texto_negritas(texto_color("❌ Opción inválida, intente de nuevo", "rojo")))
            sleep(3)

def demo_ejemplo():
    """Demostración con datos de ejemplo"""
    limpiar_pantalla()
    mostrar_banner()
    pila_fcfs = Pila()
    
    # Procesos de ejemplo
    procesos_ejemplo = [
        Proceso(1, "Navegador", 0, 5),
        Proceso(2, "Editor", 1, 3),
        Proceso(3, "Antivirus", 2, 8),
        Proceso(4, "Calculadora", 3, 2)
    ]
    
    for proceso in procesos_ejemplo:
        pila_fcfs.apilar(proceso)
    
    pila_fcfs.ejecutar_fcfs()

    sleep(2)
    input(texto_color("\nPresione Enter para regresar al menú principal...", "amarillo"))
    menu_principal()

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def texto_negritas(texto):
    return f"\033[1m{texto}\033[0m"

def texto_color(texto, color="rojo"):
    colores = {
        "rojo": "\033[31m",
        "verde": "\033[32m",
        "amarillo": "\033[33m",
        "azul": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "blanco": "\033[37m"
    }
    return f"{colores.get(color, colores['rojo'])}{texto}\033[0m"

def mostrar_banner():
    print(texto_negritas(texto_color("===========================================================================")))
    print(texto_negritas(texto_color(" ______________      ______________      ______________      _____________ ")))   
    print(texto_negritas(texto_color("|              |    |              |    |              |    |             |")))
    print(texto_negritas(texto_color("|     _________|    |     _________|    |     _________|    |     ________|")))
    print(texto_negritas(texto_color("|    |_________     |    |              |    |_________|    |    |________ ")))
    print(texto_negritas(texto_color("|              |    |    |              |              |    |             |")))
    print(texto_negritas(texto_color("|     _________|    |    |              |     _________|    |_______      |")))
    print(texto_negritas(texto_color("|    |              |    |_________     |    |               _______|     |")))
    print(texto_negritas(texto_color("|    |              |              |    |    |              |             |")))
    print(texto_negritas(texto_color("|____|              |______________|    |____|              |_____________|")))
    print(texto_negritas(texto_color("===========================================================================")))

if __name__ == "__main__":
    limpiar_pantalla()
    mostrar_banner()

    print(texto_negritas(texto_color("¿Qué desea hacer?", "azul")))
    print("1. Usar menú interactivo")
    print("2. Ver demo con datos de ejemplo")
    
    opcion = input("Seleccione: ").strip()
    
    if opcion == "1":
        limpiar_pantalla()
        sleep(5)
        menu_principal()
    elif opcion == "2":
        limpiar_pantalla()
        sleep(2)
        demo_ejemplo()
    else:
        print("Opción inválida, ejecutando demo...")
        sleep(5)
        limpiar_pantalla()
        sleep(5)
        demo_ejemplo()