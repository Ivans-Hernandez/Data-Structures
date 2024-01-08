import random # Importamos la biblioteca random para generar numero aleatorios 
import math # Bilioteca para poder realizar operaciones aritmeticas 

# Para poder calcular el elemento mas grande del arreglo 
def countingSort(arr):

    k = max(arr) # Sirve para encontrar el elemeto mas grande del arreglo 

    print("k:" , k) # Mostramos el valor de k 

    C = [0] * (k+1) # Creamos un arreglo con tantos elementos como el mayor numero del arreglo k


    for i in range(len(arr)): # Se itera tantas veces como lementos tengamos en el arreglo 
        valor = arr[i]
        C[valor] += 1

    C[0] -= 1
    for i in range(1, len(C)):  # Se itera tantas veces como elementos tengamos en el arreglo C
        C[i] = C[i] + C[i-1]
    B = [0]*len(arr)

    for j in range(len(arr)-1, -1, -1):  # Se itera al reves tantas veces como elementos tengamos en el arreglo 
        valor = arr[j]
        posicion = C[valor]
        B[posicion] = valor
        C[valor] -= 1
    return B # Retornamos el arreglo B 

a = [] # Arreglo
n = 5000 # Numero de elemtnos del arreglo 

for j in range(n): # Servira para poder llenar el arreglo
    a.append(random.randint(0,2000)) # Guarmamos los numero generados aletoriamente en el arrglo a


print("Arreglo desordenado: ", a) # Imprimimos el arreglo
print("Arreglo ordenado: ", countingSort(a)) # Llamamos a la funcion CountingSort para ordenar el arreglo


