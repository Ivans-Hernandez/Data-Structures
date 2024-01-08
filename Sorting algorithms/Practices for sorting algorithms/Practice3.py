import random # Importamos la biblioteca random para generar numero aleatorios 
import math # Bilioteca para poder realizar operaciones aritmeticas 
import time

# Para este programa tendremos las mismas 
# funciones mostradas en el ejercicio anterior

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

def radixSort(arr): # Funcion RadixSort para ordenar los elementos del arreglo 
    k = max(arr)
    d = math.floor(math.log10(k)) + 1 # Opreacion aritmetica 
    print("k: ", k, "d: ", d)

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

aa = [] # Para guardar los elementos de la lista cuando k = n/2
n= 10000

print("########### Ordenamiento para ", n, " elementos en el arreglo. ##################\n\n")

print("//////  Tiempo de ordenamiento para k:", n, "  ///////\n") # Mostramos cuantos elementos contendra la lista
print("-------- Mejor Caso (Lista aleatoria) ----------\n\n")

print("Para countingSort tenemos: \n")

for i in range(n): # El ciclo se ejecurara tantas veces como elementos tengamos en la lista 
    aa.append(random.randint(0, n//2)) # Codigo para generar numeros aleatorios del 0 a 10

a1 = aa[:] # Copiamos la lista generada para asignarlo a cada algoritmo creado
a2 = aa[:]

inicio = time.time()
mejorCounting = countingSort(a1)
fin = time.time()
tiempoFinal = fin - inicio
print(tiempoFinal, " s\n\n")

print("Para RadixSort tenemos: \n")

inicio = time.time()
mejorRadix = radixSort(a2)
fin = time.time()
tiempoFinal = fin - inicio
print(tiempoFinal, " s")


print("\n\n//////  Tiempo de ordenamiento para k:", n*10000, "  ///////\n") # Mostramos cuantos elementos contendra la lista
print("-------- Peor Caso (Lista aleatoria) ----------\n") 

ab = [] # Para guardar los elementos de la lista cuando k = n*100000

for i in range(n): # El ciclo se ejecurara tantas veces como elementos tengamos en la lista 
    ab.append(random.randint(0, n*10000))

a3 = ab[:] # Copiamos la lista generada para asignarlo a cada algoritmo creado
a4 = ab[:]

print("Para countingSort tenemos: \n")

inicio = time.time()
peorCounting = countingSort(a3)
fin = time.time()
tiempoFinal = fin - inicio
print(tiempoFinal, " s")

print("Para RadixSort tenemos: \n")

inicio = time.time()
mejorRadix = radixSort(a4)
fin = time.time()
tiempoFinal = fin - inicio
print(tiempoFinal, " s")

print("\n\n//////  Tiempo de ordenamiento para k:", n, "  ///////\n") # Mostramos cuantos elementos contendra la lista
print("-------- Caso primedio (Lista aleatoria) ----------\n") 

ac = [] # Para guardar los elementos de la lista cuando k = n

for i in range(n): # El ciclo se ejecurara tantas veces como elementos tengamos en la lista 
    ac.append(random.randint(0, n))

a5 = ac[:] # Copiamos la lista generada para asignarlo a cada algoritmo creado
a6 = ac[:]

print("Para countingSort tenemos: \n")

inicio = time.time()
promedCounting = countingSort(a5)
fin = time.time()
tiempoFinal = fin - inicio
print(tiempoFinal, " s")

print("Para RadixSort tenemos: \n")

inicio = time.time()
mejorRadix = radixSort(a6)
fin = time.time()
tiempoFinal = fin - inicio
print(tiempoFinal, " s")