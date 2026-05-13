from src.my_array import MyArray


def merge_sort(array: MyArray) -> MyArray:
    merge_sort_rec(array, 0, len(array) - 1)
    return array


def merge_sort_rec(array, inicio, fim):
    if inicio >= fim:
        return

    meio = (inicio + fim) // 2

    merge_sort_rec(array, inicio, meio)

    merge_sort_rec(array, meio + 1, fim)

    merge(array, inicio, meio, fim)


def merge(array, inicio, meio, fim):
    esquerda = []
    direita = []

    for i in range(inicio, meio + 1):
        esquerda.append(array[i])

    for i in range(meio + 1, fim + 1):
        direita.append(array[i])

    i = 0
    j = 0
    k = inicio

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            array[k] = esquerda[i]
            i += 1
        else:
            array[k] = direita[j]
            j += 1

        k += 1

    while i < len(esquerda):
        array[k] = esquerda[i]
        i += 1
        k += 1

    while j < len(direita):
        array[k] = direita[j]
        j += 1
        k += 1
