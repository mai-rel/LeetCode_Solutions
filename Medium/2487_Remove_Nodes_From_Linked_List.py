from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def reverse_list(head):
    prev_node = None
    current_node = head

    while current_node:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node

    return prev_node


def removeNodes(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head.next:
        return head

    new_head = reverse_list(head)
    pointer = new_head
    max_value = pointer.val

    while pointer.next:
        if pointer.next.val < max_value:
            pointer.next = pointer.next.next
        else:
            pointer = pointer.next
            max_value = max(max_value, pointer.val)

    return reverse_list(new_head)