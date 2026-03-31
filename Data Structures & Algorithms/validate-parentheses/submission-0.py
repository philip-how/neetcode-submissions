from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        valid_starters = ["[", "{", "("]

        get_opposites = {"]": "[", "}" : "{", ")": "("}

        stack = deque()

        for char in s:
            if char in valid_starters:
                stack.append(char)
            else:
                if len(stack) < 1:
                    return False
                if stack.pop() != get_opposites[char]:
                    return False
        
        if len(stack) > 0:
            return False

        return True 
