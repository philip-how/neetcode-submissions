# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = None
        curr = None
        while l1 is not None or l2 is not None or carry != 0:
            total = carry
            carry = 0
            if l1 is not None:
                total += l1.val
                l1 = l1.next
            if l2 is not None:
                total += l2.val
                l2 = l2.next
            
            if total > 9:
                carry = total // 10
                total = total - carry * 10

            if head is None:
                head = ListNode(total)
                curr = head
            else:
                curr.next = ListNode(total)
                curr = curr.next
            
        return head
            