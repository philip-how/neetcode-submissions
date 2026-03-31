# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        running1 = list1
        running2 = list2

        if list1 == None:
            return list2
        if list2 == None:
            return list1

        if running1.val < running2.val:
            running = ListNode(running1.val)
            running1 = running1.next
        else:
            running = ListNode(running2.val)
            running2 = running2.next

        head = running

        while running1 != None or running2 != None:
            if running1 == None:
                running.next = ListNode(running2.val)
                running = running.next
                running2 = running2.next
            elif running2 == None:
                running.next = ListNode(running1.val)
                running = running.next
                running1 = running1.next
            elif running1.val < running2.val:
                running.next = ListNode(running1.val)
                running = running.next
                running1 = running1.next
            else:
                running.next = ListNode(running2.val)
                running = running.next
                running2 = running2.next

        return head



        