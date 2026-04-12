class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        prev = None
        curr = None

        for i in range(len(s)):
            curr = [0] * len(t)
            if s[i] == t[0]:
                curr[0] = 1
            for j in range(len(t)):
                if i > 0:
                    curr[j] += prev[j]
                    if j > 0 and s[i] == t[j]:
                        curr[j] += prev[j - 1]
            prev = curr
        
        return curr[-1]
        