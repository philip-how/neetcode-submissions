class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        trailing = True
        while trailing and i >= 0:
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
            else:
                trailing = False
            i -= 1
        
        if trailing:
            digits.insert(0, 1)
            
        return digits
        