import random # Biblioteca pra generar numeros aleatorios 
import math # Sirve pra realizar mas operaciones
import time # Para obtener el tiempos de ejecucion de cada programa 
import sys # Para incrementar el limite de las recursiones 

sys.setrecursionlimit(10000) #Sirve para poder incrementar el numero de recusriones de python

################### RandomQuickSort ####################

def rQuickSort(arr, inicio , detener):
    if(inicio < detener):
        pivoteIdx = partitionrand(arr, inicio, detener)
        rQuickSort(arr , inicio , pivoteIdx-1)
        rQuickSort(arr, pivoteIdx + 1, detener)
def partitionrand(arr , inicio, detener):
    randomPivote = random.randrange(inicio, detener)
 
   
    arr[inicio], arr[randomPivote] = arr[randomPivote], arr[inicio]
    return partition(arr, inicio, detener)
def partition(arr,inicio,detener):
    pivote = inicio 

    i = inicio + 1
     
    for j in range(inicio + 1, detener + 1):
        if arr[j] <= arr[pivote]:
            arr[i] , arr[j] = arr[j] , arr[i]
            i = i + 1
    arr[pivote] , arr[i - 1] = arr[i - 1] , arr[pivote]
    pivote = i - 1
    return (pivote)

################### HeapSort ####################
def MaxHeapify(arr, i, tamañoDelHeap):
    idxIzq = 2*i
    idxDer = 2*i+1

    if(idxIzq<=(tamañoDelHeap-1) and arr[idxIzq]>arr[i]):
        posMax=idxIzq
    else:
        posMax=i
    if(idxDer<=(tamañoDelHeap-1) and arr[idxDer]>arr[posMax]):
        posMax=idxDer
    if(posMax!=i):
        intercambia(arr, i, posMax)
        MaxHeapify(arr, posMax, tamañoDelHeap)
def construirMaxHeapIni(arr, tamañoDelHeap):
    tamañoDelHeap = len(arr)
    for i in range(math.ceil((tamañoDelHeap)/2),-1,-1):
        MaxHeapify(arr, i, tamañoDelHeap)
def heapSort(arr):
    tamañoDelHeap = len(arr)
    construirMaxHeapIni(arr, tamañoDelHeap)
    for i in range(len(arr)-1,0,-1):
        intercambia(arr, 0, i)
        tamañoDelHeap-=1
        MaxHeapify(arr,0,tamañoDelHeap)
def intercambia(arr, x, y):
    arr[x],arr[y]=arr[y], arr[x]

################### QuickSort ####################

def quickSort(arr, p, r):
    if p < r:
        q = particionar(arr , p ,r)
        quickSort(arr, p, q-1)
        quickSort(arr, q+1, r)
def particionar(arr, p ,r):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if(arr[j] <= x):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1


################### Main ####################
n = 2500 # Numero de elementos que contendra la lista 
a = [] # Lista

for i in range(n): # El ciclo se ejecurara tantas veces como elementos tengamos en la lista 
    a.append(random.randint(0, n)) # Codigo para generar numeros aleatorios del 0 a n

a1 = a[:] # Copiamos la lista generada para asignarlo a cada algoritmo creado
a2 = a[:]
a3 = a[:]

print("//////  Tiempo de ordenamiento para n:", n, "  ///////\n") # Mostramos cuantos elementos contendra la lista
print("-------- Caso promedio (Lista aleatoria) ----------") # Para caso promedio


print("\n\nTiempo de ordenamiento que tarda HeapSort")
inicio = time.time() # Cronometro que nos ayudara a medir cuanto tiempo tarda cada algoritmo en ordenar los elemetos de la lista
heapSort(a1) # Llamamos al algortimo para que ordene la lista generada
fin = time.time() #Tiempo que tardara el algoritmo en ordenar los elementos de la lista
tiempoFinal = fin - inicio # Calculamos el tiempo final restando los cronometros que colocamos anteriormente 
print(tiempoFinal, " s") # Mostramo el tiempo final

# Hacemos lo mismo para medir el tiempo de ejecucion de cada algoritmo creado

print("\n\nTiempo de ordenamiento que tarda QuickSort")
inicio = time.time()
quickSort(a2, 0, len(a)-1)
fin = time.time()
tiempoFinal = fin - inicio
print(tiempoFinal, " s")

print("\n\nTiempo de ordenamiento que tarda Random Quick Sort")
inicio = time.time()
rQuickSort(a3, 0, len(a)-1)
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

print("\n\nTiempo de ordenamiento que tarda HeapSort")
inicio = time.time() # Cronometro que nos ayudara a medir cuanto tiempo tarda cada algoritmo en ordenar los elemetos de la lista
heapSort(a1) # Llamamos al algortimo para que ordene la lista generada
fin = time.time() #Tiempo que tardara el algoritmo en ordenar los elementos de la lista
tiempoFinal = fin - inicio # Calculamos el tiempo final restando los cronometros que colocamos anteriormente
print(tiempoFinal, " s") # Mostramo el tiempo final

# Hacemos lo mismo para medir el tiempo de ejecucion de cada algoritmo creado

print("\n\nTiempo de ordenamiento que tarda QuickSort")
inicio = time.time()
quickSort(a2, 0, len(a)-1)
fin = time.time()
tiempoFinal = fin - inicio
print(tiempoFinal, " s")

print("\n\nTiempo de ordenamiento que tarda Ramdom Quick Sort")
inicio = time.time()
rQuickSort(a3, 0, len(a)-1)
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

print("\n\nTiempo de ordenamiento que tarda HeapSort")
inicio = time.time() # Cronometro que nos ayudara a medir cuanto tiempo tarda cada algoritmo en ordenar los elemetos de la lista
heapSort(a1) # Llamamos al algortimo para que ordene la lista generada
fin = time.time() #Tiempo que tardara el algoritmo en ordenar los elementos de la lista
tiempoFinal = fin - inicio # Calculamos el tiempo final restando los cronometros que colocamos anteriormente
print(tiempoFinal, " s") # Mostramo el tiempo final

# Hacemos lo mismo para medir el tiempo de ejecucion de cada algoritmo creado

print("\n\nTiempo de ordenamiento que tarda QuickSort")
inicio = time.time()
quickSort(a2, 0, len(a)-1)
fin = time.time()
tiempoFinal = fin - inicio
print(tiempoFinal, " s")

print("\n\nTiempo de ordenamiento que tarda Random Quick Sort")
inicio = time.time()
rQuickSort(a3, 0, len(a)-1)
fin = time.time()
tiempoFinal = fin - inicio
print(tiempoFinal, " s")