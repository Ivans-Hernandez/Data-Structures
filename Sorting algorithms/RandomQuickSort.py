import random

def rQuickSort(arr, inicio , detener):
    if(inicio < detener):
        pivoteIdx = partitionrand(arr, inicio, detener)
        rQuickSort(arr , inicio , pivoteIdx-1)
        rQuickSort(arr, pivoteIdx + 1, detener)

def partitionrand(arr , inicio, detener):
    randomPivote = random.randrange(inicio, detener)
 
   
    arr[inicio], arr[randomPivote] = arr[randomPivote], arr[inicio]
    return partition(arr, inicio, detener)
 
def partition(arr,inicio,detener):
    pivote = inicio 

    i = inicio + 1
     
    for j in range(inicio + 1, detener + 1):
        if arr[j] <= arr[pivote]:
            arr[i] , arr[j] = arr[j] , arr[i]
            i = i + 1
    arr[pivote] , arr[i - 1] = arr[i - 1] , arr[pivote]
    pivote = i - 1
    return (pivote)

a = []
n = 50

for f in range(n):
    a.append(random.randint(0, n))

print("Arreglo desordenado: ", a)
rQuickSort(a, 0, len(a)-1)
print("Arreglo ordenado: ", a)



