import random

def busquedaLinealMejorada(arr, key): #Funcion para encontrear la llave
    idx = None # Asignosmos None debido a que si no encuntra la llave buscada nos mostrar que no la encontro
    for i in range(len(arr)): # Iteramos tantas veces como elementos tengamos en el arreglo
        if arr[i] == key: # Comparamos los elementos del arreglo
            return i # Si encontramos el elemento buscado regresamos dicho elemento
    return idx # No encontramos el elemento buscado (key)

# Codigo para asignar los elemento del arreglo y la llave
a = []
n = 10
for i in range(n):
    a.append(random.randint(0, n))

print("a: ", a)
key = 10
encontrar = busquedaLinealMejorada(a, key)
print("La llave es: ", key, "\nFue encontrada? ", encontrar)
