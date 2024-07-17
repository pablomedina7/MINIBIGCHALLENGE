import random
import time

# Función para particionar el array usando la mediana de tres como pivote
def media_de_tres(arr, low, high):
    mid = (low + high) // 2
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    return mid

def particion (arr, low, high):
    mid = media_de_tres(arr, low, high)
    arr[mid], arr[high] = arr[high], arr[mid]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        pi = particion (arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

# Generar conjuntos de datos aleatorios
conjuntoP = random.sample(range(1000), 100)
conjuntoM = random.sample(range(1000), 300)
conjuntoG = random.sample(range(1000), 500)

# Función para medir el tiempo de ejecución y el uso de memoria
def measure_performance_and_memory(dataset):
    start_time = time.perf_counter()
    quickSort(dataset, 0, len(dataset) - 1)
    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000  # en milisegundos

    # Calcular el uso de memoria estimado
    memory_usage = len(dataset) * 8 / 1024  # asumimos 8 bytes por elemento (tamaño de referencia)
    return execution_time, memory_usage

# Medir el rendimiento para cada conjunto de datos y mostrar los resultados
def measure_and_print_results(dataset, label):
    time_ms, memory_kb = measure_performance_and_memory(dataset.copy())
    print(f"{label}:")
    print(f"Tiempo de Ejecución: {time_ms:.11f} ms")
    print(f"Uso de Memoria: {memory_kb:.4f} KB")
    print()

# Mostrar los resultados para cada conjunto de datos
measure_and_print_results(conjuntoP, "Conjunto Pequeño (100 elementos)")
measure_and_print_results(conjuntoM, "Conjunto Mediano (300 elementos)")
measure_and_print_results(conjuntoG, "Conjunto Grande (500 elementos)")

