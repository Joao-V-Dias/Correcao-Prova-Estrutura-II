def selection_sort_inverse(array):
    n = len(array) - 1
    for i in range(n, -1, -1):
        indexMenor = i
        for j in range(0, i - 1):
            if array[j] < array[indexMenor]:
                indexMenor = j
        array[i], array[indexMenor] = array[indexMenor], array[i]

array = [11, 4, 30, 22, 7, 26]
selection_sort_inverse(array)
print(array)