# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer = head

        size = 0

        while pointer is not None:
            size += 1
            pointer = pointer.next

        pointer = head

        if size - n == 0:
            return pointer.next

        i = 0
        while i < size - n - 1:
            pointer = pointer.next
            i += 1
        
        pointer.next = pointer.next.next
        
        return head