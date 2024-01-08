import random
import math

def MaxHeapify(arr, i, tamañoDelHeap): # funcion maxHepify
    idxIzq = 2*i # Indice izquierdo del arreglo
    idxDer = 2*i+1 # Indice derecho del arreglo

    # Comparamos cual es el indice Max
    if(idxIzq<=(tamañoDelHeap-1) and arr[idxIzq]>arr[i]):
        posMax=idxIzq
    else:
        posMax=i
    if(idxDer<=(tamañoDelHeap-1) and arr[idxDer]>arr[posMax]):
        posMax=idxDer
    # Si posMax es diferente de i intercambiamos los elementos y llamamos recusrivamente a maxHepify  
    if(posMax!=i):
        intercambia(arr, i, posMax)
        MaxHeapify(arr, posMax, tamañoDelHeap)

def construirMaxHeapIni(arr, tamañoDelHeap): # construirMaxHeapIni
    tamañoDelHeap = len(arr) # tamaño del arreglo
    for i in range(math.ceil((tamañoDelHeap)/2),-1,-1): # de atras hacia adelante iteramos
        MaxHeapify(arr, i, tamañoDelHeap) # Llamamos a max heapify para cada uno de los datos 

def heapSort(arr):
    tamañoDelHeap = len(arr) # Tamaño del arreglo 
    construirMaxHeapIni(arr, tamañoDelHeap) # Construimos el maxHeapIni
    for i in range(len(arr)-1,0,-1): # iteramos de atras hacia denlante 
        intercambia(arr, 0, i) # Intermabiamos los elementos del arreglo 
        tamañoDelHeap-=1 # Restamos los elemetnos del arreglo que ya estan ordenados 
        MaxHeapify(arr,0,tamañoDelHeap) # Llamamos a maxHepify 

def intercambia(arr, x, y): # Funcion para intecmabiar los elementos del arreglo 
    arr[x],arr[y]=arr[y], arr[x]

# Main del programa para ordenar los elementos con heapSort 
a = []
elementos = 30

for k in range(elementos):
   a.append(random.randint(0,elementos))

print("Arreglo generado: ", a, "\n")
heapSort(a)
print("Arreglo ordenado: ", a)

