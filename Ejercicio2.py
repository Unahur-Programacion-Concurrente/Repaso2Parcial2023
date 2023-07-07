import threading
import random
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

# Estructura básica de un Monitor
# Variables locales (privadas) o permanentes (static) - Recursos
# Código de Inicialización (constructor)
# Procedimientos Internos (privados)
# Procedimientos exportados (publicos) - Todos con exclusión mútua (synchronized)

# Variables locales (privadas) - Recursos y Estado
# Código de Inicialización (constructor)
class listaMonitor():
    def __init__(self):
        self.__lista = []
        self.__lock = threading.RLock()
        self.__maxConsumos = threading.Condition(self.__lock)
        self.__fueConsumido = True
        self.__consumido = threading.Condition(self.__lock)
        self.__consumos = 0
        self.__semaforoConsumos = threading.Semaphore(2)

# Procedimientos exportados (publicos)
    def leerLista(self):
        with self.__lock:
            while self.__consumos == 2:
                self.__maxConsumos.wait()
            self.__consumos += 1
            self.__fueConsumido = True
            self.__consumido.notify_all()
            return self.__lista

    def llenarLista(self, valores):
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
    def __init__(self, monitorL):
        super().__init__()
        self.listaM = monitorL
        self.milista = []

    def run(self):
        while True:
            for _ in range(5):
                self.milista.append(random.randint(0,100))
            self.listaM.llenarLista(self.milista)
            logging.info(f'asignó los valores  {self.milista}')
            time.sleep(2)


class consumidor(threading.Thread):
    def __init__(self, monitorL):
        super().__init__()
        self.listaM = monitorL
        self.milista = []

    def run(self):
        while True:
            self.milista = self.listaM.leerLista()
            for k in range(5):
                logging.info(f'Calculo index{k} = {self.milista[k]**2} ')
            time.sleep(1)


mon = listaMonitor()
hilos = []
for _ in range(3):
    prod = productor(mon)
    hilos.append(prod)
    cons = consumidor(mon)
    hilos.append(cons)

for hilo in hilos:
    hilo.start()
