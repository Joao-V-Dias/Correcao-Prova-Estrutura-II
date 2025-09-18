def insertion_sort_recursivo(array, n = 1):
    if n >= len(array):
        return
    x = array[n]
    j = n - 1
    while j >= 0 and array[j] > x:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = x
    insertion_sort_recursivo(array, n + 1)
