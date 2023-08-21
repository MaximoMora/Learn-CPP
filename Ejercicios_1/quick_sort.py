El codigo corresponde al algoritmo Quick Sort, indica linea por linea como en los ejemplos anteriores la complejidad algoritmica Big O:

def partition(arr, low, high):
    pivot = arr[high]   # big(1)
    i = (low - 1)       # big(1)

    for j in range(low, high): #big(n)
                                                                                 # Si el elemento actual es más pequeño o igual al pivot
        if arr[j] <= pivot:    #big n 
            i = i + 1          #big n 
            arr[i], arr[j] = arr[j], arr[i]  #big n                      # Intercambio #big(1)

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # big 1                       # Intercambio big(1)
    return (i + 1) #big 1

def quick_sort(arr, low, high):
    if low < high:      #big(1)
                                                                            # pi es el índice de particionamiento
        pi = partition(arr, low, high) #big o n

                                                                                                    # Ordenar separadamente los elementos antes y después del índice de particionamiento
        quick_sort(arr, low, pi - 1)  #big n/2
        quick_sort(arr, pi + 1, high) #big n/2



        #big n/

# Código de prueba
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quick_sort(arr, 0, n - 1)
print("El arreglo ordenado es:", arr)
