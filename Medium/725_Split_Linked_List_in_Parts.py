from typing import List, Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def splitListToParts(head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
    if not head:
        return [head] * k

    total = 0
    p = head

    while p:
        total += 1
        p = p.next

    nodes_in_part = total // k
    r = total % k
    result = []

    start = head
    p = head
    size = 1

    while start:
        target_size = nodes_in_part
        if r:
            target_size = nodes_in_part + 1
            r -= 1

        while size < target_size:
            p = p.next
            size += 1

        result.append(start)
        start = p.next
        p.next = None
        p = start
        size = 1

    empty_parts = k - len(result)
    if empty_parts:
        result.extend([None] * empty_parts)

    return result