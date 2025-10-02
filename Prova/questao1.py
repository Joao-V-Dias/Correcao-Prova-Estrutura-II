def inserir_ordenado(array, x):
    array.append(x)
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


array = []
inserir_ordenado(array, 6)
print(array)

array = [11, 4, 30, 22, 7, 26]
inserir_ordenado(array, -1)
print(array)

array = [11, 4, 30, 22, 7, 26]
inserir_ordenado(array, 1000)
print(array)

array = [11, 4, 30, 22, 7, 26]
inserir_ordenado(array, 30)
print(array)