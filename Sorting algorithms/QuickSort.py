import random
import sys

sys.setrecursionlimit(1000000)

def quickSort(arr, p, r):
    if p < r:
        q = particionar(arr , p ,r)
        quickSort(arr, p, q-1) # Llamamos reursivamente a quicksort
        quickSort(arr, q+1, r)

def particionar(arr, p ,r):
    x = arr[r] # Ultimo elemento del arreglo
    i = p - 1 # Para el sub arreglo izquierdo
    for j in range(p, r):
        if(arr[j] <= x):
            i += 1
            arr[i], arr[j] = arr[j], arr[i] # Intecambiamos los elementos del arreglo
    arr[i+1], arr[r] = arr[r], arr[i+1] # Volvemos a intecarmbiar los elementos del arreglo
    return i+1 # Retornamos la ultima posicion el pivote

n = 20
a = []

for k in range(n):
    a.append(random.randint(0,n))

print("Arreglo desordenado: ", a)
quickSort(a, 0, len(a)-1)
print("Arreglo ordenado: ", a)
