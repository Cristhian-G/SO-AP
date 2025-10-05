class Proceso:
    def __init__(self, pid, nombre, tiempo_llegada, tiempo_ejecucion):
        self.estado = 'nuevo' 
        self.pid = pid
        self.nombre = nombre
        self.tiempo_llegada = tiempo_llegada
        self.tiempo_ejecucion = tiempo_ejecucion
        self.tiempo_ejecucion_original = tiempo_ejecucion 
        self.tiempo_finalizacion = 0
        self.tiempo_espera = 0
        self.tiempo_inicio = 0  # Cuándo empezó a ejecutarse

    def __str__(self):
        return f"Proceso(pid={self.pid}, nombre={self.nombre}, estado={self.estado}, tiempo_llegada={self.tiempo_llegada}, tiempo_ejecucion={self.tiempo_ejecucion}, tiempo_finalizacion={self.tiempo_finalizacion}, tiempo_espera={self.tiempo_espera})" 
    
    def contador(self):
        if self.tiempo_ejecucion > 0:
            self.tiempo_ejecucion -= 1
            if self.tiempo_ejecucion == 0:
                self.estado = 'terminado'
        return self.tiempo_ejecucion
    
    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def get_estado(self):
        return self.estado
    
    def get_pid(self):
        return self.pid
    
    def get_nombre(self):
        return self.nombre
    
    def get_tiempo_llegada(self):
        return self.tiempo_llegada
    
    def get_tiempo_ejecucion(self):
        return self.tiempo_ejecucion
    
    def set_tiempo_ejecucion(self, nuevo_tiempo):
        self.tiempo_ejecucion = nuevo_tiempo

    def ejecutar_proceso(self, tiempo_actual):
        if self.tiempo_ejecucion > 0:
            self.estado = 'ejecutando'
            self.tiempo_ejecucion -= 1
            if self.tiempo_ejecucion == 0:
                self.estado = 'terminado'
                self.tiempo_finalizacion = tiempo_actual + 1
                self.tiempo_espera = self.tiempo_finalizacion - self.tiempo_llegada - self.tiempo_ejecucion_original
        return self.tiempo_ejecucion == 0
