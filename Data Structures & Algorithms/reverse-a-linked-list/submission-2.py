# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        prev = None
        running = head

        while running != None:
            running_next = running.next
            running.next = prev

            prev = running
            running = running_next

        return prev


        
        