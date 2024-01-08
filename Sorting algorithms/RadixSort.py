import random # Importamos la biblioteca random para generar numero aleatorios 
import math # Bilioteca para poder realizar operaciones aritmetica

def radixSort(arr): # Funcion RadixSort para ordenar los elementos del arreglo 
    k = max(arr)
    d = math.floor(math.log10(k)) + 1 # Opreacion aritmetica 
    print("k: ", k, "d: ", d)

    for i in range(d):
        arr = rSort(arr, 10, i)
        print("arr en la itaracion ", i," es ",  arr)
    return arr

#Funcion para poder ordenar los elementos del arreglo, comparando las unidedes, decenas, centenas y milesimas
def rSort(arr, b, i):
    k = b - 1
    C = [0] * (k + 1)

    for j in range(len(arr)): # For que se ejetara segun el tamaño del arreglo 
        valor = arr[j]
        digit = math.floor(valor/math.pow(b ,i)) % b # Opreacion aritmetica para calcular al numero mayor del arreglo 
        C[digit] += 1
    C[0] -= 1

    # Calcular la Frecuencia acumulada 
    for j in range(1, len(C)):
        C[j] = C[j] + C[j-1]

    B = [0] * (len(arr))

    for j in range(len(arr)-1, -1, -1): # For para hacer la regresion al reves
        valor = arr[j]
        digit = math.floor(valor/math.pow(b ,i)) % b # Opreacion aritmetica 
        posicion = C[digit]
        B[posicion] = valor

        C[digit] -= 1

    return B

a = [] # Arreglo
n = 10 # Numero de elemtnos del arreglo 

for i in range (n): # Servira para poder llenar el arreglo
    a.append(random.randint(0, 2000)) # Guarmamos los numero generados aletoriamente en el arrglo a

print("Arreglo desordenado: ", a) # Imprimimos el arreglo
print("arreglo ordenado", radixSort(a)) # Llamamos a la funcion RadixSort para ordenar el arreglo


