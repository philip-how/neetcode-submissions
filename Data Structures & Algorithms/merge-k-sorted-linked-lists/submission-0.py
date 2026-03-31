# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        output_head = None
        output_current = None
        while not self.allNone(lists):
            lowest_ls = -1
            lowest_val = 1001
            i = 0
            while i < len(lists):
                if lists[i] is None:
                    i += 1
                    continue
                
                if lists[i].val < lowest_val:
                    lowest_val = lists[i].val
                    lowest_ls = i
                i += 1
            
            if output_current is None:
                output_head = lists[lowest_ls]
                output_current = output_head
            else:
                output_current.next = lists[lowest_ls]
                output_current = lists[lowest_ls]
            
            lists[lowest_ls] = lists[lowest_ls].next
        
        return output_head



    def allNone(self, lists: List[Optional[ListNode]]) -> bool:
        for ls in lists:
            if ls is not None:
                return False
        return True
        