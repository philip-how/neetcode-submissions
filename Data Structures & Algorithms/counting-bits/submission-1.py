class Solution:
    def countBits(self, n: int) -> List[int]:
        ls = [0] * (n+1)
        for i in range(n+1):
            ls[i] = ls[i >> 1] + (i & 1) 
            # first one: get value without last binary char
            # second one: get value of last binary char
        return ls