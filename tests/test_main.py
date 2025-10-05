# Tests para el proyecto SO-AP
# Aquí puedes agregar tus tests unitarios

import unittest
import sys
import os
from io import StringIO
from unittest.mock import patch

# Agregar el directorio app al path para poder importar los módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

from app.proceso import Proceso
from app.pila import Pila

class TestProceso(unittest.TestCase):
    """Tests para la clase Proceso"""
    
    def setUp(self):
        """Configuración inicial para cada test"""
        self.proceso = Proceso(1, "Test", 0, 5)
    
    def test_inicializacion_proceso(self):
        """Test de inicialización correcta del proceso"""
        self.assertEqual(self.proceso.pid, 1)
        self.assertEqual(self.proceso.nombre, "Test")
        self.assertEqual(self.proceso.tiempo_llegada, 0)
        self.assertEqual(self.proceso.tiempo_ejecucion, 5)
        self.assertEqual(self.proceso.tiempo_ejecucion_original, 5)
        self.assertEqual(self.proceso.estado, 'nuevo')
        self.assertEqual(self.proceso.tiempo_finalizacion, 0)
        self.assertEqual(self.proceso.tiempo_espera, 0)
    
    def test_str_representation(self):
        """Test de representación en string del proceso"""
        resultado = str(self.proceso)
        self.assertIn("pid=1", resultado)
        self.assertIn("nombre=Test", resultado)
        self.assertIn("estado=nuevo", resultado)
    
    def test_getters(self):
        """Test de métodos getter"""
        self.assertEqual(self.proceso.get_pid(), 1)
        self.assertEqual(self.proceso.get_nombre(), "Test")
        self.assertEqual(self.proceso.get_tiempo_llegada(), 0)
        self.assertEqual(self.proceso.get_tiempo_ejecucion(), 5)
        self.assertEqual(self.proceso.get_estado(), 'nuevo')
    
    def test_cambiar_estado(self):
        """Test de cambio de estado"""
        self.proceso.cambiar_estado('ejecutando')
        self.assertEqual(self.proceso.estado, 'ejecutando')
        
        self.proceso.cambiar_estado('terminado')
        self.assertEqual(self.proceso.estado, 'terminado')
    
    def test_set_tiempo_ejecucion(self):
        """Test de setter para tiempo de ejecución"""
        self.proceso.set_tiempo_ejecucion(3)
        self.assertEqual(self.proceso.tiempo_ejecucion, 3)
    
    def test_contador(self):
        """Test del método contador"""
        tiempo_inicial = self.proceso.tiempo_ejecucion
        tiempo_restante = self.proceso.contador()
        
        self.assertEqual(tiempo_restante, tiempo_inicial - 1)
        self.assertEqual(self.proceso.tiempo_ejecucion, tiempo_inicial - 1)
    
    def test_contador_hasta_terminado(self):
        """Test del contador hasta que el proceso termine"""
        # Ejecutar hasta que el proceso termine
        while self.proceso.tiempo_ejecucion > 1:
            self.proceso.contador()
        
        # Último contador que debe cambiar el estado a 'terminado'
        self.proceso.contador()
        self.assertEqual(self.proceso.estado, 'terminado')
        self.assertEqual(self.proceso.tiempo_ejecucion, 0)
    
    def test_ejecutar_proceso(self):
        """Test del método ejecutar_proceso"""
        tiempo_actual = 5
        
        # El proceso no debe terminar en la primera ejecución
        termino = self.proceso.ejecutar_proceso(tiempo_actual)
        self.assertFalse(termino)
        self.assertEqual(self.proceso.estado, 'ejecutando')
        self.assertEqual(self.proceso.tiempo_ejecucion, 4)
        
        # Ejecutar hasta que termine
        for i in range(4):
            termino = self.proceso.ejecutar_proceso(tiempo_actual + i + 1)
        
        self.assertTrue(termino)
        self.assertEqual(self.proceso.estado, 'terminado')
        self.assertEqual(self.proceso.tiempo_ejecucion, 0)


class TestPila(unittest.TestCase):
    """Tests para la clase Pila (Planificador FCFS)"""
    
    def setUp(self):
        """Configuración inicial para cada test"""
        self.pila = Pila()
        self.proceso1 = Proceso(1, "Proceso1", 0, 3)
        self.proceso2 = Proceso(2, "Proceso2", 1, 2)
        self.proceso3 = Proceso(3, "Proceso3", 2, 4)
    
    def test_inicializacion_pila(self):
        """Test de inicialización de la pila"""
        self.assertEqual(len(self.pila.procesos), 0)
        self.assertEqual(self.pila.tiempo_actual, 0)
        self.assertEqual(len(self.pila.procesos_terminados), 0)
        self.assertTrue(self.pila.esta_vacia())
    
    def test_apilar_proceso(self):
        """Test de apilar un proceso"""
        self.pila.apilar(self.proceso1)
        self.assertEqual(self.pila.tamano(), 1)
        self.assertFalse(self.pila.esta_vacia())
    
    def test_apilar_multiple_procesos_orden_fcfs(self):
        """Test de apilar múltiples procesos y verificar orden FCFS"""
        # Agregar procesos en orden diferente al tiempo de llegada
        self.pila.apilar(self.proceso3)  # tiempo_llegada = 2
        self.pila.apilar(self.proceso1)  # tiempo_llegada = 0
        self.pila.apilar(self.proceso2)  # tiempo_llegada = 1
        
        # Verificar que estén ordenados por tiempo de llegada
        self.assertEqual(self.pila.procesos[0].tiempo_llegada, 0)  # proceso1
        self.assertEqual(self.pila.procesos[1].tiempo_llegada, 1)  # proceso2
        self.assertEqual(self.pila.procesos[2].tiempo_llegada, 2)  # proceso3
    
    def test_ver_tope(self):
        """Test de ver el tope de la pila (siguiente proceso en FCFS)"""
        self.pila.apilar(self.proceso2)
        self.pila.apilar(self.proceso1)
        
        tope = self.pila.ver_tope()
        self.assertEqual(tope.pid, 1)  # proceso1 tiene menor tiempo de llegada
    
    def test_ver_tope_pila_vacia(self):
        """Test de ver tope en pila vacía"""
        with self.assertRaises(IndexError):
            self.pila.ver_tope()
    
    def test_desapilar(self):
        """Test de desapilar proceso"""
        self.pila.apilar(self.proceso1)
        self.pila.apilar(self.proceso2)
        
        proceso_desapilado = self.pila.desapilar()
        self.assertEqual(proceso_desapilado.pid, 1)  # proceso1 (menor tiempo llegada)
        self.assertEqual(self.pila.tamano(), 1)
    
    def test_desapilar_pila_vacia(self):
        """Test de desapilar en pila vacía"""
        with self.assertRaises(IndexError):
            self.pila.desapilar()
    
    def test_obtener_proceso_listo(self):
        """Test de obtener proceso listo para ejecutar"""
        self.pila.apilar(self.proceso1)  # tiempo_llegada = 0
        self.pila.apilar(self.proceso2)  # tiempo_llegada = 1
        
        # En tiempo 0, solo proceso1 está listo
        self.pila.tiempo_actual = 0
        proceso_listo = self.pila.obtener_proceso_listo()
        self.assertEqual(proceso_listo.pid, 1)
        
        # En tiempo 1, proceso1 sigue siendo el primero (FCFS)
        self.pila.tiempo_actual = 1
        proceso_listo = self.pila.obtener_proceso_listo()
        self.assertEqual(proceso_listo.pid, 1)
    
    def test_obtener_proceso_listo_ninguno_disponible(self):
        """Test cuando no hay procesos listos"""
        proceso_futuro = Proceso(4, "Futuro", 10, 2)
        self.pila.apilar(proceso_futuro)
        
        self.pila.tiempo_actual = 5  # Antes del tiempo de llegada
        proceso_listo = self.pila.obtener_proceso_listo()
        self.assertIsNone(proceso_listo)
    
    def test_reiniciar(self):
        """Test de reiniciar la pila"""
        self.pila.apilar(self.proceso1)
        self.pila.tiempo_actual = 5
        self.pila.procesos_terminados.append(self.proceso2)
        
        self.pila.reiniciar()
        
        self.assertEqual(len(self.pila.procesos), 0)
        self.assertEqual(self.pila.tiempo_actual, 0)
        self.assertEqual(len(self.pila.procesos_terminados), 0)
        self.assertTrue(self.pila.esta_vacia())
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_mostrar_cola_con_procesos(self, mock_stdout):
        """Test de mostrar cola con procesos"""
        self.pila.apilar(self.proceso1)
        self.pila.apilar(self.proceso2)
        
        self.pila.mostrar_cola()
        output = mock_stdout.getvalue()
        
        self.assertIn("PID: 1", output)
        self.assertIn("PID: 2", output)
        self.assertIn("Proceso1", output)
        self.assertIn("Proceso2", output)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_mostrar_cola_vacia(self, mock_stdout):
        """Test de mostrar cola vacía"""
        self.pila.mostrar_cola()
        output = mock_stdout.getvalue()
        
        self.assertIn("No hay procesos en la cola", output)
    
    def test_ejecutar_proceso_privado(self):
        """Test del método privado _ejecutar_proceso"""
        proceso = Proceso(1, "Test", 0, 2)
        
        # Primera ejecución
        termino = self.pila._ejecutar_proceso(proceso)
        self.assertFalse(termino)
        self.assertEqual(proceso.estado, 'ejecutando')
        self.assertEqual(proceso.tiempo_ejecucion, 1)
        
        # Segunda ejecución (debería terminar)
        self.pila.tiempo_actual = 1
        termino = self.pila._ejecutar_proceso(proceso)
        self.assertTrue(termino)
        self.assertEqual(proceso.estado, 'terminado')
        self.assertEqual(proceso.tiempo_ejecucion, 0)


class TestIntegracionFCFS(unittest.TestCase):
    """Tests de integración para el algoritmo FCFS completo"""
    
    def setUp(self):
        """Configuración para tests de integración"""
        self.pila = Pila()
    
    def test_escenario_fcfs_basico(self):
        """Test de escenario básico FCFS con 3 procesos"""
        # Crear procesos con diferentes tiempos de llegada
        p1 = Proceso(1, "P1", 0, 2)  # Llega en 0, dura 2
        p2 = Proceso(2, "P2", 1, 3)  # Llega en 1, dura 3
        p3 = Proceso(3, "P3", 3, 1)  # Llega en 3, dura 1
        
        self.pila.apilar(p1)
        self.pila.apilar(p2)
        self.pila.apilar(p3)
        
        # Simular ejecución completa usando la lógica corregida
        proceso_actual = None
        
        while self.pila.procesos or proceso_actual:
            # Buscar proceso si no hay uno actual
            if not proceso_actual:
                siguiente = self.pila.obtener_proceso_listo()
                if siguiente:
                    siguiente.estado = 'listo'
                    proceso_actual = siguiente
                    self.pila.procesos.remove(siguiente)
            
            # Ejecutar proceso actual
            if proceso_actual:
                termino = self.pila._ejecutar_proceso(proceso_actual)
                if termino:
                    self.pila.procesos_terminados.append(proceso_actual)
                    proceso_actual = None
            
            # Avanzar tiempo
            self.pila.tiempo_actual += 1
        
        # Verificar que todos los procesos terminaron
        self.assertEqual(len(self.pila.procesos_terminados), 3)
        
        # Verificar orden de finalización (FCFS)
        self.assertEqual(self.pila.procesos_terminados[0].pid, 1)  # P1 primero
        self.assertEqual(self.pila.procesos_terminados[1].pid, 2)  # P2 segundo
        self.assertEqual(self.pila.procesos_terminados[2].pid, 3)  # P3 tercero
        
        # Verificar tiempos de finalización según los valores verificados:
        self.assertEqual(self.pila.procesos_terminados[0].tiempo_finalizacion, 1)  # P1: termina en 1
        self.assertEqual(self.pila.procesos_terminados[1].tiempo_finalizacion, 4)  # P2: termina en 4
        self.assertEqual(self.pila.procesos_terminados[2].tiempo_finalizacion, 5)  # P3: termina en 5
    
    def test_calculo_metricas_fcfs(self):
        """Test de cálculo correcto de métricas FCFS"""
        # Proceso simple para verificar cálculos
        proceso = Proceso(1, "Test", 2, 3)  # Llega en 2, dura 3
        self.pila.apilar(proceso)
        
        # Simular ejecución completa siguiendo la lógica corregida
        proceso_actual = None
        
        while self.pila.procesos or proceso_actual:
            # Buscar proceso si no hay uno actual
            if not proceso_actual:
                siguiente = self.pila.obtener_proceso_listo()
                if siguiente:
                    siguiente.estado = 'listo'
                    proceso_actual = siguiente
                    self.pila.procesos.remove(siguiente)
            
            # Ejecutar proceso actual
            if proceso_actual:
                termino = self.pila._ejecutar_proceso(proceso_actual)
                if termino:
                    break
            
            # Avanzar tiempo
            self.pila.tiempo_actual += 1
        
        # Verificar métricas según los valores verificados
        self.assertEqual(proceso.tiempo_finalizacion, 4)  # Termina en tiempo 4
        self.assertEqual(proceso.tiempo_espera, 0)  # No hay espera (llega en 2, empieza en 2)


def suite():
    """Crear suite de tests"""
    suite = unittest.TestSuite()
    
    # Agregar tests de Proceso
    suite.addTest(unittest.makeSuite(TestProceso))
    
    # Agregar tests de Pila
    suite.addTest(unittest.makeSuite(TestPila))
    
    # Agregar tests de integración
    suite.addTest(unittest.makeSuite(TestIntegracionFCFS))
    
    return suite


if __name__ == '__main__':
    # Ejecutar todos los tests
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
    
    # O ejecutar tests individuales
    # unittest.main(verbosity=2)