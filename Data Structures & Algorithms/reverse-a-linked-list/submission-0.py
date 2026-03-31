# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        running = ListNode(head.val)

        running_real = head.next

        while running_real != None:
            running = ListNode(running_real.val, running)
            running_real = running_real.next

        return running


        
        