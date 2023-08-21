El codigo corresponde al algoritmo Quick Sort, indica linea por linea como en los ejemplos anteriores la complejidad algoritmica Big O:

def partition(arr, low, high):
    pivot = arr[high]   # Tomamos el último elemento como pivot
    i = (low - 1)       # índice del elemento más pequeño

    for j in range(low, high):
        # Si el elemento actual es más pequeño o igual al pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]  # Intercambio

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Intercambio
    return (i + 1)

def quick_sort(arr, low, high):
    if low < high:
        # pi es el índice de particionamiento
        pi = partition(arr, low, high)

        # Ordenar separadamente los elementos antes y después del índice de particionamiento
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Código de prueba
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quick_sort(arr, 0, n - 1)
print("El arreglo ordenado es:", arr)
