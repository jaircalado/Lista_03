from src.my_node import MyNode


def has_cycle(head: MyNode) -> bool:
    if head is None:
        return False
    
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

