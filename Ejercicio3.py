import threading
import random
import time
import logging
import queue
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

# Monitor (clase)

# Estructura básica de un Monitor
# Variables locales (privadas) o permanentes (static) - Recursos
# Código de Inicialización (constructor)
# Procedimientos Internos (privados)
# Procedimientos Exportados (publicos) - Todos con exclusión mútua (synchronized)


class listaMonitor():
    def __init__(self):
        self.__lista = []
        self.__lock = threading.RLock()
        self.__maxConsumos = threading.Condition(self.__lock)
        self.__fueConsumido = False
        self.__consumido = threading.Condition(self.__lock)
        self.__consumos = 0
        #self.__semaforoConsumos = threading.Semaphore(2)

# Procedimientos Exportados
    def leerLista(self):
        #Obtengo el lock para leer la lista
        with self.__lock:
            while self.__consumos == 2:
                self.__maxConsumos.wait()
            self.__consumos += 1
            self.__fueConsumido = True
            self.__consumido.notify_all()
            return self.__lista

    def llenarLista(self, valores):
        #Obtengo el lock para modificar la lista
        with self.__lock:
            while self.__consumos < 2:
                self.__consumido.wait()
            self.__lista.clear()
            self.__lista = valores
            self.__fueConsumido = False
            self.__consumos = 0
            self.__maxConsumos.notify_all()


    def appendLista(self, valor):
        with self.__lock:
            self.__lista.append(valor)


class productor(threading.Thread):

    def __init__(self, monitor):
        super().__init__()
        self.listaM = monitor
        self.miLista = []

    def run(self):
        while True:
            for _ in range(5):
                self.miLista.append(random.randint(0,100))
            self.listaM.llenarLista(self.miLista)
            logging.info(f'Lleno la lista con los datos = {self.miLista}')
            time.sleep(2)

class consumidor(threading.Thread):

    def __init__(self, monitor):
        super().__init__()
        self.listaM = monitor
        self.miLista = []

    def run(self):
        while True:
            self.miLista = self.listaM.leerLista()
            for indice, valor in enumerate(self.miLista):
                executor.submit(self.calculaCuadrado(indice,valor))
            time.sleep(1)

    def calculaCuadrado(self, indice, valor):
        logging.info(f'Calculo item-{indice} = {valor**2}')



mon = listaMonitor()

hilos = []

executor = ThreadPoolExecutor(max_workers=5)

for _ in range(10):
    prod = productor(mon)
    hilos.append(prod)
    cons = consumidor(mon)
    hilos.append(cons)

for hilo in hilos:
    hilo.start()

for hilo in hilos:
    hilo.join()
