import random
import time 

def busquedaLinealMejorada(arr, key): #Funcion para encontrear la llave
    idx = None # Asignosmos None debido a que si no encuntra la llave buscada nos mostrar que no la encontro
    for i in range(len(arr)): # Iteramos tantas veces como elementos tengamos en el arreglo
        if arr[i] == key: # Comparamos los elementos del arreglo
            return i # Si encontramos el elemento buscado regresamos dicho elemento
    return idx # No encontramos el elemento buscado (key)

def busquedaLinealCentilena(arr, key):
    n = len(arr) # n almacenara el tamaño del arreglo
    ultimo = arr[n-1] # Almacenra el ultimo elemento del arreglo menos 1
    arr[n-1] = key # Igualamos la llave al ultimo elemento del arreglo menos 1

    i = 0

    while arr[i] != key: # Se itera mientas el elemento en i sea diferente de la llave que buscamos
        i += 1           # Recorremos la lista hasta encontrar el elemento buscado

    encontrar = None # Le asignamos nada en caso de no encontrar la llave :v 

    if(i < n-1) or (ultimo == key): # Comparamos si el elemento encontrado es el buscado
        encontrar = i # Felicidades encontarte al amor de tu vida, ok no, nadamas a la llave :,v

    arr[n - 1] = ultimo # Cuando la llave no se encunetra en el arreglo
    return encontrar # Retornamos que no encontramos el elemento :(

def busquedaBinariaRecursiva(arr, llave, idxIzq, idxDer):
    if idxIzq > idxDer: # Caso base 
        return None
    centro = (idxIzq+idxDer)//2 # Calculamos el ventro del arreglo 
    if arr[centro] == llave: # Cuando el elemento del centro es igual al elemetnos buscado 
        return centro # Retornamos el elemento encontrado
    elif llave < arr[centro]: # Buscamos por el lado izq del arreglo la llave 
        # Actualizamos los elementos de los arreglos y llamamos recursivamente a la funcion 
        return busquedaBinariaRecursiva(arr, llave, idxIzq, centro - 1) 
    else:
        return busquedaBinariaRecursiva(arr, llave, centro + 1, idxDer)

# Primero generamos el arreglo al cual despues le haremos 3 copias para asignar a cada 
# algoritmo y asi todos tengan el mismo arreglo 

a = []
n = 1000000

for i in range(n): # El ciclo se ejecurara tantas veces como elementos tengamos en la lista 
    a.append(random.randint(0, n//2)) # Llenamos a lista de elementos

# Generamos una llave aleatoria
llaveAleatoria = random.randint(0, n//2)

print("//////  Tiempo de ordenamiento para n:", n, "  ///////\n")
print("/////La llave generada aleatoriamente es: ", llaveAleatoria, "//////\n")

print("\n\nTiempo que tarda Busqueda lineal mejorada")
inicio = time.perf_counter() # Cronometro que nos ayudara a medir cuanto tiempo tarda cada algoritmo en ordenar los elemetos de la lista
busquedaLinealMejorada(a, llaveAleatoria) # Llamamos al algortimo para que ordene la lista generada
fin = time.perf_counter() #Tiempo que tardara el algoritmo en ordenar los elementos de la lista
tiempoFinal = fin - inicio # Calculamos el tiempo final restando los cronometros que colocamos anteriormente 
print(tiempoFinal, " s\n") # Mostramo el tiempo final

# Hacemos lo mismo para medir el tiempo de ejecucion de cada algoritmo creado

print("\n\nTiempo que tarda Busqueda lineal con centinela")
inicio = time.perf_counter()
busquedaLinealCentilena(a, llaveAleatoria)
fin = time.perf_counter()
tiempoFinal = fin - inicio
print(tiempoFinal, " s\n")

print("\n\nTiempo Tiempo que tarda Busqueda binaria")
inicio = time.perf_counter()
busquedaBinariaRecursiva(a, llaveAleatoria, 0, len(a)-1)
fin = time.perf_counter()
tiempoFinal = fin - inicio
print(tiempoFinal, " s")