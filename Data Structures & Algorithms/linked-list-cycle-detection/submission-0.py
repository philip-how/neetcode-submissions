# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.index = None
        

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        index = 0
        pointer = head

        while pointer != None:
            if pointer.index is not None:
                return True
            else:
                pointer.index = index
            
            pointer = pointer.next
            
            index += 1
        
        return False
            