from src.my_node import MyNode


def kth_to_last(head: MyNode, k: int) -> int:
    slow = head
    fast = head

    for _ in range(k):
        if fast is None:
            return -1
        
        fast = fast.next

    while fast is not None:
        slow = slow.next
        fast = fast.next

    if slow is None:
        return -1

    return slow.value
