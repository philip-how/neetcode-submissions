# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.old_next = None
        self.prev = None
        self.visited = False

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        pointer = head
        prev = None

        while pointer != None:
            pointer.old_next = pointer.next
            pointer.next = None
            pointer.prev = prev
            prev = pointer
            pointer = pointer.old_next

        end = prev
        start = head


        running_pointer = None

        while start != end and (not start.visited) and (not end.visited):
            if running_pointer is None:
                running_pointer = start
                start.visited = True
                start = start.old_next
            else:
                running_pointer.next = start
                running_pointer = running_pointer.next

                start.visited = True
                start = start.old_next

            running_pointer.next = end

            running_pointer = running_pointer.next

            end.visited = True
            end = end.prev
        
        if running_pointer is None:
            running_pointer = start
        elif start == end:
            running_pointer.next = start
        
        pointer = head

        i = 0

        while i < 10 and pointer != None:
            print(pointer.val)

            pointer = pointer.next
            i += 1
        
        
            



        