from questao1 import verifica
from questao2 import bubble_sort
from questao6 import insertion_sort
from questao7 import insertion_sort_recursivo

def main():
    print(verifica(array1))
    bubble_sort(array1)
    print(array1)
    insertion_sort(array2)
    print(array2)
    insertion_sort_recursivo(array3)
    print(array3)

array1 = [4, 5, 6, 7, 8, 3]
array2 = [1, 8, 9, 7, 4, 6]
array3 = [9, 8, 7, 6, 5, 4]

main()