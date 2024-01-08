import math # Importamos la biblioteca math para generar calcular math.floor
import random # Importamos la biblioteca random para generar numeros aleatorios
import time

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

n = 2000000 # Numero de elementos que contendra la lista 
a = [] # Lista

for i in range(n): # El ciclo se ejecurara tantas veces como elementos tengamos en la lista 
    a.append(random.randint(0, 10)) # Codigo para generar numeros aleatorios del 0 a 10

a1 = a[:] # Copiamos la lista generada para asignarlo a cada algoritmo creado
a2 = a[:]
a3 = a[:]

print("//////  Tiempo de ordenamiento para n:", n, "  ///////\n") # Mostramos cuantos elementos contendra la lista
print("-------- Caso promedio (Lista aleatoria) ----------") # Para caso promedio


inicio = time.time() # Cronometro que nos ayudara a medir cuanto tiempo tarda cada algoritmo en ordenar los elemetos de la lista
mergeSort(a1, 0, len(a1)-1) # Llamamos al algortimo para que ordene la lista generada
fin = time.time() #Tiempo que tardara el algoritmo en ordenar los elementos de la lista
tiempoFinal = fin - inicio # Calculamos el tiempo final restando los cronometros que colocamos anteriormente 
print(tiempoFinal, " s") # Mostramo el tiempo final

print("-------- Mejor caso (Lista ordenada asc) ----------") # Codigo para medir el mejor caso ordenado asc

a = []

for m in range(n): # Creamos la lista ordenada asc para medir los tiempo de ordenamiento
    a.append(m)

a1= a[:] # Copiamos la lista generada para asignarlo a cada algoritmo creado

inicio = time.time() # Cronometro que nos ayudara a medir cuanto tiempo tarda cada algoritmo en ordenar los elemetos de la lista
mergeSort(a1, 0, len(a1)-1) # Llamamos al algortimo para que ordene la lista generada
fin = time.time() #Tiempo que tardara el algoritmo en ordenar los elementos de la lista
tiempoFinal = fin - inicio # Calculamos el tiempo final restando los cronometros que colocamos anteriormente
print(tiempoFinal, " s") # Mostramo el tiempo final


print("-------- Peor caso (Lista ordenada desc) ----------")

a = []

for v in range(n-1, 0, -1): # Creamos la lista ordenada desc para medir los tiempo de ordenamiento
    a.append(v)

a1= a[:] # Copiamos la lista generada para asignarlo a cada algoritmo creado
a2= a[:]
a3= a[:]

inicio = time.time() # Cronometro que nos ayudara a medir cuanto tiempo tarda cada algoritmo en ordenar los elemetos de la lista
mergeSort(a1, 0, len(a1)-1) # Llamamos al algortimo para que ordene la lista generada
fin = time.time() #Tiempo que tardara el algoritmo en ordenar los elementos de la lista
tiempoFinal = fin - inicio # Calculamos el tiempo final restando los cronometros que colocamos anteriormente
print(tiempoFinal, " s") # Mostramo el tiempo final