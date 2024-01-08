import random # Importamos la biblioteca random para generar numeros aleatorios

def bubbleSort( arr ): # Funcion bubbleSort para ordenar listas, recible como argumento una lista
    n = len(arr)       # contamos el numero de elementos que contiene la lista 
    # Codigo para ordenar los elemetnos de la lista 
    for i in range(n - 1):
        for j in range(n - 1):
            if arr[j] > arr[j+1]:

                aux = arr[j] #Asi se programaria en C
                arr[j] = arr[j+1]
                arr[j+1] = aux

                #Sintaxis sugar de python :o
                # arr[j], arr[j+1] = arr[j+1], arr[j] 

n = 10 # Numero de elementos que contendra la lista 
a = [] 

for i in range(n):
    a.append(random.randint(0, 10)) # Sintaxis sugar de Python para generar numeros aleatorios
    # a.append lo que hace es que manda a guarda al arreglo a los numeros randoms generados por random.randint
    # a[i] = random.randint(1, 9) Asi de programaria en C


print("\nArreglo desordenado: ", a, "\n") # Mostramos el arrglo desordenado y generado aleatoriamente 

bubbleSort(a) # LLamamos a nuestra funcion bubbleSort para que ordene el arreglo 
print("Arreglo ordenado: ", a, "\n") # Mostamos el arreglo ordenado 
