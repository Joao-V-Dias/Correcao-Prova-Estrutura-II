def bubble_sort(array):
    tamanho = len(array)
    for i in range(tamanho):
        flag = True
        for j in range(tamanho-i-1):
            if array[j] > array[j+1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = False
        if flag == True:
            break