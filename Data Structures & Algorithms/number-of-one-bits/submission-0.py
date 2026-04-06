class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        running_minus = 0
        for i in range(32):
            if n % 2**(i+1) - running_minus:
                count += 1
                running_minus += 2**i
        
        return count