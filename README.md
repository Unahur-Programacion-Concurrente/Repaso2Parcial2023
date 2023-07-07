# Repaso Segundo Parcial 2023

## Ejercicio 1

Escriba un programa que ejecute los siguientes hilos que utilizan datos almacenados en una **lista de 5 elementos**.

**<u>Productor</u>**: ejecuta un bucle infinito en el cual carga cinco valores enteros aleatorios (entre 0 y 100) en la lista e imprime en pantalla un mensaje identificando al hilo y el contenido de la lista. Por ejemplo:
```
Thread-9 asignó los valores  [1, 2, 3, 4, 5]
```
**<u>Consumidor</u>**: ejecuta un bucle infinito en el que calcula la suma de todos los elementos de la lista  y la imprime en un mensaje que incluya la identificación del hilo. Por ejemplo:
```
Thread-2 calculo la suma = 15
```

Utilizando Monitores, implementar la concurrencia del programa de modo que:

- Los hilos **productores** deben esperar hasta que **por lo menos uno y no más que dos** consumidores consuman los valores de la lista.
- Los hilos **consumidores** deben esperar a que algún productor asigne nuevos valores a la lista si el contenido actual ya fue consumido por uno o dos consumidores.
- El hilo principal debe arrancar por lo menos 10 hilos de cada tipo (Productor y Consumidor).


## Ejercicio 2

Escriba un programa que ejecute los siguientes hilos que utilizan datos almacenados en una **lista de 5 elementos**.

**<u>Productor</u>**: ejecuta un bucle infinito en el cual carga cinco valores enteros aleatorios (entre 0 y 100) en la lista e imprime en pantalla un mensaje identificando al hilo y el contenido de la lista. Por ejemplo:
```
Thread-9 asignó los valores  [1, 2, 3, 4, 5]
```
**<u>Consumidor</u>**: ejecuta un bucle infinito  en el que calcula el cuadrado de cada elemento de la lista y los imprime en lineas diferentes indicando el indice del elemento. El mensaje debe incluir la identificación del hilo. Por ejemplo:
```
Thread-2 calculo item-0 = 1
Thread-2 calculo item-1 = 4
Thread-2 calculo item-2 = 9
Thread-2 calculo item-3 = 16
Thread-2 calculo item-4 = 25
```

Utilizando Monitores, implementar la concurrencia del programa de modo que:

- Los hilos **productores** deben esperar hasta que **por lo menos dos** consumidores consuman los valores de la lista.
- Los hilos **consumidores** deben esperar a que algún productor asigne nuevos valores a la lista si el contenido actual ya fue consumido por otros dos consumidores.
- El hilo principal debe arrancar por lo menos 3 hilos de cada tipo (Productor y Consumidor).


## Ejercicio 3

Escriba un programa que ejecute los siguientes hilos que utilizan datos almacenados en una **lista de 5 elementos**.

**<u>Productor</u>**: ejecuta un bucle infinito en el cual carga cinco valores enteros aleatorios (entre 0 y 100) en la lista e imprime en pantalla un mensaje identificando al hilo y el contenido de la lista. Por ejemplo:
```
Thread-9 asignó los valores  [1, 2, 3, 4, 5]
```
**<u>Consumidor</u>**: ejecuta un bucle infinito  en el que calcula el cuadrado de cada elemento de la lista y los imprime en lineas diferentes indicando el indice del elemento. El mensaje debe incluir la identificación del hilo. Por ejemplo:
```
Thread-2 calculo item-0 = 1
Thread-2 calculo item-1 = 4
Thread-2 calculo item-2 = 9
Thread-2 calculo item-3 = 16
Thread-2 calculo item-4 = 25
```

***Esta operación debe realizarse con 5 worker threads que hagan el calculo y la impresión en paralelo***.

Utilizando Monitores, implementar la concurrencia del programa de modo que:

- Los hilos **productores** deben esperar hasta que **por lo menos un consumidor** consuma los valores de la lista.
- Los hilos **consumidores** deben esperar a que **un productor** asigne nuevos valores a la lista si el contenido actual ya fue consumido por otro consumidor.
- El hilo principal debe arrancar por lo menos 3 hilos de cada tipo (Productor y Consumidor).
