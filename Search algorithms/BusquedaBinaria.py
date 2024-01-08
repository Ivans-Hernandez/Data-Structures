import random
import math

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

a = []
n = 10
for i in range(n):
    a.append(random.randint(0, n))

print("a: ", a)
key = 10
encontrar = busquedaBinariaRecursiva(a, key, 0, len(a)- 1)
print("La llave es: ", key, "\nFue encontrada? ", encontrar)