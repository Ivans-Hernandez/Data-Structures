import random

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

# Main

a = []
n = 10
for i in range(n):
    a.append(random.randint(0, n))

print("a: ", a)
key = 10
encontrar = busquedaLinealCentilena(a, key)
print("La llave es: ", key, "\nFue encontrada? ", encontrar)