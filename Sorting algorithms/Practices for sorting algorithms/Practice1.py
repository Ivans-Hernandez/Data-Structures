import time
import math
import random

#Funcion MergerSort
def mergeSort( arr, p, r): #Indice del ultimo elemento r
    if p < r :
        q= math.floor((p + r) / 2 )
        mergeSort( arr, p, q )
        mergeSort( arr, q+1, r )
        merge(arr,p,q,r)

# Funcion merger
def merge(arr,p,q,r): 
    # Dividimos la lista a la mitad
    izq = arr[p: q+1] 
    der = arr[q+1: r+1]

    i = 0
    j = 0

    # Comenzamos a divir la lista en elementos mas pequeños para luego comenzar a ordenarlos y juntar 
    # cada elemento en una sola lista ya ordenada
    for k in range(p, r+1):
        if (j >= r -q ) or (( i < q-p+1) and izq[i] < der[j]):
            arr[k] = izq[i]
            i += 1
        else:
            arr[k] = der[j]
            j += 1

# Funcion bubbleSort
def bubbleSort( arr ): # Funcion bubbleSort para ordenar listas, recible como argumento una lista
    n = len(arr)       # contamos el numero de elementos que contiene la lista 
    # Codigo para ordenar los elemetnos de la lista 
    for i in range(n - 1):
        for j in range(n - 1):
            if arr[j] > arr[j+1]:

                #Sintaxis sugar de python :o
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Funcion bubbleSortOptimizada
def bubbleSortOp(arr):
    n = len(arr)
    i = 1
    ordenado = False

    while(i < n and ordenado == False): # Verificamos que la lista contenga elementos para ordenar
        i = i + 1
        ordenado = True
        for j in range( n - 1): # Comenzamos a ordenar la lista que reciba la funcion 
            if(arr[j] > arr[j+1]):
                ordenado = False
                arr[j], arr[j+1] = arr[j+1], arr[j]

n = 5000 # Numero de elementos que contendra la lista 
a = [] # Lista

for i in range(n): # El ciclo se ejecurara tantas veces como elementos tengamos en la lista 
    a.append(random.randint(0, 10)) # Codigo para generar numeros aleatorios del 0 a 10

a1 = a[:] # Copiamos la lista generada para asignarlo a cada algoritmo creado
a2 = a[:]
a3 = a[:]

print("//////  Tiempo de ordenamiento para n:", n, "  ///////\n") # Mostramos cuantos elementos contendra la lista
print("-------- Caso promedio (Lista aleatoria) ----------") # Para caso promedio


print("\n\nTiempo de ordenamiento que tarda MergerSort")
inicio = time.time() # Cronometro que nos ayudara a medir cuanto tiempo tarda cada algoritmo en ordenar los elemetos de la lista
mergeSort(a1, 0, len(a1)-1) # Llamamos al algortimo para que ordene la lista generada
fin = time.time() #Tiempo que tardara el algoritmo en ordenar los elementos de la lista
tiempoFinal = fin - inicio # Calculamos el tiempo final restando los cronometros que colocamos anteriormente 
print(tiempoFinal, " s") # Mostramo el tiempo final

# Hacemos lo mismo para medir el tiempo de ejecucion de cada algoritmo creado

print("\n\nTiempo de ordenamiento que tarda BubbleSort")
inicio = time.time()
bubbleSort(a2)
fin = time.time()
tiempoFinal = fin - inicio
print(tiempoFinal, " s")

print("\n\nTiempo de ordenamiento que tarda BubbleSort Optimozado ")
inicio = time.time()
bubbleSortOp(a3)
fin = time.time()
tiempoFinal = fin - inicio
print(tiempoFinal, " s\n\n")

print("-------- Mejor caso (Lista ordenada asc) ----------") # Codigo para medir el mejor caso ordenado asc

a = []

for m in range(n): # Creamos la lista ordenada asc para medir los tiempo de ordenamiento
    a.append(m)

a1= a[:] # Copiamos la lista generada para asignarlo a cada algoritmo creado
a2= a[:]
a3= a[:]

print("\n\nTiempo de ordenamiento que tarda MergerSort")
inicio = time.time() # Cronometro que nos ayudara a medir cuanto tiempo tarda cada algoritmo en ordenar los elemetos de la lista
mergeSort(a1, 0, len(a1)-1) # Llamamos al algortimo para que ordene la lista generada
fin = time.time() #Tiempo que tardara el algoritmo en ordenar los elementos de la lista
tiempoFinal = fin - inicio # Calculamos el tiempo final restando los cronometros que colocamos anteriormente
print(tiempoFinal, " s") # Mostramo el tiempo final

# Hacemos lo mismo para medir el tiempo de ejecucion de cada algoritmo creado

print("\n\nTiempo de ordenamiento que tarda BubbleSort")
inicio = time.time()
bubbleSort(a2)
fin = time.time()
tiempoFinal = fin - inicio
print(tiempoFinal, " s")

print("\n\nTiempo de ordenamiento que tarda BubbleSort Optimozado")
inicio = time.time()
bubbleSortOp(a3)
fin = time.time()
tiempoFinal = fin - inicio
print(tiempoFinal, " s\n\n")


print("-------- Peor caso (Lista ordenada desc) ----------")

a = []

for v in range(n-1, 0, -1): # Creamos la lista ordenada desc para medir los tiempo de ordenamiento
    a.append(v)

a1= a[:] # Copiamos la lista generada para asignarlo a cada algoritmo creado
a2= a[:]
a3= a[:]

print("\n\nTiempo de ordenamiento que tarda MergerSort")
inicio = time.time() # Cronometro que nos ayudara a medir cuanto tiempo tarda cada algoritmo en ordenar los elemetos de la lista
mergeSort(a1, 0, len(a1)-1) # Llamamos al algortimo para que ordene la lista generada
fin = time.time() #Tiempo que tardara el algoritmo en ordenar los elementos de la lista
tiempoFinal = fin - inicio # Calculamos el tiempo final restando los cronometros que colocamos anteriormente
print(tiempoFinal, " s") # Mostramo el tiempo final

# Hacemos lo mismo para medir el tiempo de ejecucion de cada algoritmo creado

print("\n\nTiempo de ordenamiento que tarda BubbleSort")
inicio = time.time()
bubbleSort(a2)
fin = time.time()
tiempoFinal = fin - inicio
print(tiempoFinal, " s")

print("\n\nTiempo de ordenamiento que tarda BubbleSort Optimozado")
inicio = time.time()
bubbleSortOp(a3)
fin = time.time()
tiempoFinal = fin - inicio
print(tiempoFinal, " s")