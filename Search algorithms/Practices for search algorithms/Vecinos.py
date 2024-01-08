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

# Modificamos busqueda binaria 
def busquedaBinaria(arr, llave, idxIzq, idxDer):
    encontrar = None
    idxMax = None

    while idxIzq <= idxDer:
        centro = (idxIzq+idxDer) // 2
        if llave == arr[centro]:
            idxMax = centro 
            return idxMax, encontrar
        else:
            if arr[centro] < llave:
                idxIzq = centro + 1
            else:
                idxDer = centro - 1 
        if idxMax == None:
            arr.append(llave)
            idxIzq = 0
            idxDer = len(arr)-1
            arr.sort()

            while idxDer <= idxIzq:
                centro = (idxIzq+idxDer)//2
                if llave == arr[centro]:
                    idxMax = centro
                    encontrar = False
                    return idxMax, encontrar
                else:
                    if arr[centro]< llave:
                        idxIzq = centro + 1
                    else: 
                        idxDer = centro - 1

def comprobar(arrTemporal, m, x):
    while len(arrTemporal) > m:
        if len(arrTemporal) == m:
            break
        if abs(arrTemporal[0] - x) < abs(arrTemporal[ len( arrTemporal - 1) - x]):
            del arrTemporal[len(arrTemporal) - 1]
        elif abs(arrTemporal[0] - x ) == abs(arrTemporal[len(arrTemporal) - 1] - x):
            del arrTemporal[0]
        elif abs(arrTemporal[0] - x ) ==abs(arrTemporal[len(arrTemporal) - 1 ] - x):
            del arrTemporal[len(arrTemporal) - 1]
    return arrTemporal

def busquedaBinariaVecinos(arr, x, r, m):
    arrTemporal = []

    idxMax, encontar = busquedaBinaria(arr, x , 0, len(arr)-1)

    if idxMax == 0:
        here = 0
        y = 0
        if encontar == False:
            here = 1 
            y = 1
        for i in range(here, m + y, 1):
            if abs(arr[idxMax+i] - x) <= r:
                arrTemporal.append(arr[idxMax+i])
        return comprobar(arrTemporal, m, x)
    else:
        here = 0
        y = 0
        if(encontar == False):
            here = 1 
            y = 1
        for j in range(1, m+1, 1):
            if idxMax-j == -1:
                break
            if abs(arr[idxMax-j]-x) <= r:
                arrTemporal.insert(0, arr[idxMax-j])
        for j  in range(here, m+y, 1):
            if idxMax+j == len(arr):
                break
            if abs(arr[idxMax+j]-x) <= r:
                arrTemporal.append(arr[idxMax+j])
    return comprobar(arrTemporal, m, x)

def BusquedaLinealVecinos(arr, x, r, m):
    arrTemporal = []
    idxMax = busquedaLinealCentilena(arr, x)
    if idxMax == -1:
        return arrTemporal
    if idxMax == 0:
        for j in range(0, m, 1):
            if abs(arr[idxMax+j]-x) <= r:
                arrTemporal.append(arr[idxMax+j])
            return comprobar(arrTemporal, m, x)

    else:
        for j in range(0, m, 1):
            if (idxMax-j) == -1:
                return arrTemporal
            if abs(arr[idxMax-j]-x) <= r:
                arrTemporal.insert(0,arr[idxMax-j])
        for j in range(1, m, 1):
            if abs(arr[idxMax+j]-x) <= r:
                arrTemporal.append(arr[idxMax+j])
        return comprobar(arrTemporal, m, x)

n = 30
busqueda = 15
r = 5
m = 10
a = []

for k in range(0, n):
    a.append(random.randint(0,n))

print("////////////// Para busqueda con centinela ////////////////////////")
print(a)
print("Vecinos del valor buscado: ", busqueda)
print("Vecinos cercanos: ", BusquedaLinealVecinos(a, busqueda, r, m))

print("\n\n////////////// Para busqueda binaria ////////////////////////")
print(a)
print("Vecinos del valor buscado: ", busqueda)

print("Vecinos cercanos: ", busquedaBinariaVecinos(a, busqueda, r, m))



