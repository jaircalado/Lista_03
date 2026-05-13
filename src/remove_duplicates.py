from src.my_node import MyNode


def remove_duplicates(head: MyNode) -> MyNode:
    atual = head

    while atual is not None:
        anterior = atual
        comparador = atual.next

        while comparador is not None:

            # Se encontrar duplicata
            if comparador.value == atual.value:
                anterior.next = comparador.next
                comparador = comparador.next
            else:
                anterior = comparador
                comparador = comparador.next

        atual = atual.next

    return head
