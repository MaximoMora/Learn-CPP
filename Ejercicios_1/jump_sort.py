import math

def jump_search(arr, x):
    n = len(arr)

    # Definir el tamaño del salto
    step = math.sqrt(n)

    # Encontrar el bloque donde podría estar el elemento
    prev = 0
    while arr[int(min(step, n)-1)] < x:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1

    # Búsqueda lineal en el bloque
    for i in range(int(prev), int(min(step, n))):
        if arr[i] == x:
            return i
    return -1

# Código de prueba
arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
x = 55
print(f"El número {x} está en el índice {jump_search(arr, x)}")