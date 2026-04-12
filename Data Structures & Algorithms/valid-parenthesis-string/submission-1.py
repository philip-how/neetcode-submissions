from collections import deque

class Solution:
    def checkValidString(self, s: str) -> bool:
        star_stack = deque()
        left_parenth_stack = []

        for i, char in enumerate(s):
            # at the end, greatest star stack indices will
            # be most useful to eat left parenth

            if char == "(":
                left_parenth_stack.append(i)
            
            if char == ")":
                if len(left_parenth_stack) > 0:
                    left_parenth_stack.pop()
                elif len(star_stack) > 0:
                    star_stack.popleft()
                else:
                    return False

            if char == "*":
                star_stack.append(i)
        
        while len(left_parenth_stack) > 0:
            if len(star_stack) == 0:
                return False

            if star_stack.pop() < left_parenth_stack.pop():
                return False

        return True


