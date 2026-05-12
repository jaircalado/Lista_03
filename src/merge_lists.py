from src.my_node import MyNode


def merge_lists(lista1: MyNode, lista2: MyNode) -> MyNode:
    if lista1 is None:
        return lista2

    if lista2 is None:
        return lista1

    if lista1.value < lista2.value:
        head = lista1
        lista1 = lista1.next
    else:
        head = lista2
        lista2 = lista2.next

    atual = head

    while lista1 is not None and lista2 is not None:
        if lista1.value < lista2.value:
            atual.next = lista1
            lista1 = lista1.next
        else:
            atual.next = lista2
            lista2 = lista2.next

        atual = atual.next

    if lista1 is not None:
        atual.next = lista1
    else:
        atual.next = lista2

    return head
