class Solution:
    def countSubstrings(self, s: str) -> int:
        pal_count = 0
        for i in range(len(s)):
            j = 0
            while j <= i and j + i < len(s) and s[i-j] == s[i+j]:
                pal_count += 1
                j += 1
            
            if i > 0 and s[i-1] == s[i]:
                j = 0
                while j + 1 <= i and j + i < len(s) and s[i-j-1] == s[i+j]:
                    pal_count += 1
                    j += 1
        
        return pal_count

