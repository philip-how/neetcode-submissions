class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        best = 0

        prev = {}

        window_start = 0
        i = 0
        while i < len(s):
            if s[i] in prev and prev[s[i]] >= window_start:
                window_start = prev[s[i]] + 1
                prev[s[i]] = i
            else:
                if i - window_start + 1 > best:
                    best = i - window_start + 1
                prev[s[i]] = i
            i += 1
        
        return best
        