import random # Importamos la biblioteca random para generar numeros aleatorios

# Funcion para ordenar los elementos de la lista 
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

n = 10 # Numero de elementos que contendra la lista 
a = [] # Lista

for i in range(n): # El ciclo se ejecurara tantas veces como elementos tengamos en la lista 
    a.append(random.randint(0, 10)) # Codigo para generar numeros aleatorios del 1 a 9

print("\nArreglo desordenado: ", a, "\n") # Mostramos el arreglo desordenado y generado aleatoriamente 

bubbleSortOp(a) # Llamamos a nuestra funcion bubbleSortOptimizado para que ordene nuestra lista generada
print("Arreglo ordenado: ", a, "\n") # Mostramos la lista ordenada