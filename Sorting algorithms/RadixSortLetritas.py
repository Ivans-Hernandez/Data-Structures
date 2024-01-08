
def RadixSortLetritas( arr ):

    arrCadena = max(arr, key=len) # Obtenemos el String mas largo del arreglo y le asignamos k 
    d = len(arrCadena) # Obtenemos la longuitud de la cadena k y la igualamos a d
    for i in range( len(arr) ): # Iteramos tantas veces como elementos tenemos en el arreglo
        while len(arr[i]) < d:      
            arr[i] = arr[i] + " "    
    for i in range( d-1,-1,-1 ): # Sirve para iterar el for de atras hacia adelante tantas veces como es el valor de d     
        arr = rSort( arr, len(arr), i )  

    # Codigo para poder eliminar los espacios que puedan dejar dentro de los elementos del arreglo
    contadorIndice = 0 # Servira para contar los indices de la lista 
    for cadena in arr:     
        i=len(cadena) - 1    
        contEspacios = 0  # Servira para contar los espacios de cada string del arreglo
        
        while i > -1:   # Iteramos el while alreves para que cuente los elementos de la cadena  
            if cadena[i] == ' ':  # Si encontramos espacios en la cadena  
                contEspacios += 1
            else:    
                break   
            i -= 1   # Le restamos uno para que vaya iterando letra por letra de la cadena al revez 
        
        if contEspacios >= 1: # Sirve para comparar si el contador de espacios contiene elementos 
            aux = cadena[ : - 1 * contEspacios]   
            arr[contadorIndice] = aux  
        
        contadorIndice += 1 # Le sumamos uno al contador para que vaya iterando cada indice de la lista 

    return arr    

def rSort( arr,b,i ):
    
    C = [0]*256   # Arreglo para almacenar k elementos con tantos elementos como la tabla ASCII 

    for j in range( b ):
        cadena = arr[j]          
        valor = ord(cadena[i])    
        C[valor] += 1     

    # Calcular la Frecuencia acumulada  
    for j in range( 1, len(C) ):
        C[j] += C[j-1]   
    B = [0]*b 
    
    for j in range( b-1,-1,-1 ): # Arreglo que se iterara de antras hacia adelante 
        cadena = arr[j]               
        valor = ord(cadena[i])         
        posicion = C[valor]  
        B[posicion - 1] = cadena        
        C[valor] -= 1 
    return B


a = ["Scarlett Johansson", "Chris Hemsworth", "Chris Evans", "Robert Downey Jr", "Mark Ruffalo", "Jeremy Renner", "Brie Larson",
"Paul Rudd", "Karen Gillan", "Don Cheadle", "Tom Holland", "Elizabeth Olsen"] 

print()
print("\t/////////// RadixSort para ordenar Strings /////////////")   

print("\nArreglo Desordenado:\n", a) # Mostramos el arreglo desordenado 
# Llamamos a la funcion radixSortLetritas para odernar el arreglo 
print("\nArreglo Ordenado:\n", RadixSortLetritas(a))   # Mostramos la lista ordenada 



