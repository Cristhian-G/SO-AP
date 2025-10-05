class Pila:
    def __init__(self):
        self.procesos = []
        self.tiempo_actual = 0
        self.procesos_terminados = []

    def apilar(self, proceso):
        """Agrega un proceso y mantiene orden FCFS (por tiempo de llegada)"""
        self.procesos.append(proceso)
        # Ordenar por tiempo de llegada para FCFS
        self.procesos.sort(key=lambda p: p.tiempo_llegada)

    def desapilar(self):
        if not self.esta_vacia():
            return self.procesos.pop(0)  # Sacar del frente para FCFS
        raise IndexError("La pila está vacía")

    def esta_vacia(self):
        return len(self.procesos) == 0

    def ver_tope(self):
        """En FCFS, el 'tope' es el proceso con menor tiempo de llegada"""
        if not self.esta_vacia():
            return self.procesos[0]  # Primer elemento (menor tiempo de llegada)
        raise IndexError("La pila está vacía")

    def tamano(self):
        return len(self.procesos)

    def obtener_proceso_listo(self):
        """Obtiene el siguiente proceso listo para ejecutar según FCFS"""
        for proceso in self.procesos:
            if proceso.tiempo_llegada <= self.tiempo_actual and proceso.estado == 'nuevo':
                return proceso
        return None

    def ejecutar_fcfs(self):
        """Ejecuta el algoritmo FCFS completo"""
        print("\n\033[1m\033[32m=== EJECUCIÓN ALGORITMO FCFS ===\033[0m\n")
        print(f"{'Tiempo':<8} {'Proceso':<15} {'Estado':<12} {'Tiempo Rest.':<12}")
        print("-" * 50)
        
        proceso_actual = None
        
        while self.procesos or proceso_actual:
            # Si no hay proceso ejecutándose, obtener el siguiente
            if not proceso_actual:
                siguiente = self.obtener_proceso_listo()
                if siguiente:
                    siguiente.estado = 'listo'
                    proceso_actual = siguiente
                    self.procesos.remove(siguiente)
            
            # Mostrar estado actual
            if proceso_actual:
                print(f"{self.tiempo_actual:<8} {proceso_actual.nombre:<15} {proceso_actual.estado:<12} {proceso_actual.tiempo_ejecucion:<12}")
                
                # Ejecutar el proceso
                termino = self._ejecutar_proceso(proceso_actual)
                
                if termino:
                    print(f"{self.tiempo_actual:<8} {proceso_actual.nombre:<15} {'terminado':<12} {'0':<12}")
                    self.procesos_terminados.append(proceso_actual)
                    proceso_actual = None
            else:
                print(f"{self.tiempo_actual:<8} {'CPU IDLE':<15} {'esperando':<12} {'-':<12}")
            
            # Avanzar tiempo
            self.tiempo_actual += 1
        
        self.mostrar_metricas()

    def _ejecutar_proceso(self, proceso):
        """Ejecuta un proceso por 1 unidad de tiempo"""
        if proceso.tiempo_ejecucion > 0:
            # Si es la primera vez que se ejecuta, marcar tiempo de inicio
            if proceso.estado != 'ejecutando':
                proceso.tiempo_inicio = self.tiempo_actual
            
            proceso.estado = 'ejecutando'
            proceso.tiempo_ejecucion -= 1
            
            if proceso.tiempo_ejecucion == 0:
                proceso.estado = 'terminado'
                # El tiempo de finalización es exactamente el tiempo actual
                proceso.tiempo_finalizacion = self.tiempo_actual
                # Tiempo de espera = tiempo_inicio - tiempo_llegada
                proceso.tiempo_espera = proceso.tiempo_inicio - proceso.tiempo_llegada
        return proceso.tiempo_ejecucion == 0

    def mostrar_metricas(self):
        """Muestra las métricas del algoritmo FCFS"""
        print("\n\033[1m\033[33m=== MÉTRICAS DEL ALGORITMO ===\033[0m")
        print(f"{'Proceso':<12} {'T.Llegada':<12} {'T.Ejecución':<12} {'T.Finalización':<15} {'T.Espera':<10}")
        print("-" * 70)
        
        tiempo_espera_total = 0
        tiempo_retorno_total = 0
        
        for proceso in self.procesos_terminados:
            tiempo_retorno = proceso.tiempo_finalizacion - proceso.tiempo_llegada
            tiempo_retorno_total += tiempo_retorno
            tiempo_espera_total += proceso.tiempo_espera
            
            print(f"{proceso.nombre:<12} {proceso.tiempo_llegada:<12} {proceso.tiempo_ejecucion_original:<12} {proceso.tiempo_finalizacion:<15} {proceso.tiempo_espera:<10}")
        
        n_procesos = len(self.procesos_terminados)
        if n_procesos > 0:
            print(f"\n\033[1m\033[36mTiempo promedio de espera: {tiempo_espera_total/n_procesos:.2f}\033[0m")
            print(f"\033[1m\033[36mTiempo promedio de retorno: {tiempo_retorno_total/n_procesos:.2f}\033[0m")

    def mostrar_cola(self):
        """Muestra los procesos en la cola"""
        if self.procesos:
            for i, proceso in enumerate(self.procesos, 1):
                print(f"{i}. PID: {proceso.pid}, Nombre: {proceso.nombre}, T.Llegada: {proceso.tiempo_llegada}, T.Ejecución: {proceso.tiempo_ejecucion}")
        else:
            print("\033[1m\033[31mNo hay procesos en la cola\033[0m")

    def reiniciar(self):
        """Reinicia la pila para una nueva simulación"""
        self.procesos = []
        self.tiempo_actual = 0
        self.procesos_terminados = []