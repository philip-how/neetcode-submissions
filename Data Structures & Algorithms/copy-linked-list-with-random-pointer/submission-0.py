"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        new_linked_list = []
        indexes = {}
        new_head = None
        curr = None

        ptr = head

        i = 0
        while ptr is not None:
            indexes[ptr] = i
            if new_head is None:
                new_head = Node(ptr.val)
                curr = new_head
            else:
                curr.next = Node(ptr.val)
                curr = curr.next
            new_linked_list.append(curr)
            ptr = ptr.next
            i += 1
        
        ptr = head

        i = 0
        while ptr is not None:
            if ptr.random is not None:
                new_linked_list[i].random = new_linked_list[indexes[ptr.random]]
            i += 1
            ptr = ptr.next
        
        return new_head


