from src.my_array import MyArray


def quick_sort(array: MyArray) -> MyArray:
    quick_sort_rec(array, 0, len(array) - 1)
    return array


def quick_sort_rec(array, inicio, fim):

    if inicio < fim:

        # Encontra posição correta do pivô
        pivo_index = partition(array, inicio, fim)

        # Ordena lados esquerdo e direito
        quick_sort_rec(array, inicio, pivo_index - 1)
        quick_sort_rec(array, pivo_index + 1, fim)


def partition(array, inicio, fim):

    pivo = array[fim]
    i = inicio - 1

    for j in range(inicio, fim):

        if array[j] <= pivo:
            i += 1

            # Troca elementos
            array[i], array[j] = array[j], array[i]

    # Coloca pivô na posição correta
    array[i + 1], array[fim] = array[fim], array[i + 1]

    return i + 1
