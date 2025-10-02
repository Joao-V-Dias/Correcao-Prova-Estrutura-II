def insert_sort(array):
    n = len(array)
    for i in range(1, n):
        nome = array[i]
        j = i - 1
        while j >= 0 and len(nome) < len(array[j]):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = nome


nomes = ["Ana", "Roberto", "Beatriz", "Joao", "Clara", "Lu"]
insert_sort(nomes)
print(nomes)