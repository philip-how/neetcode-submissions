class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_pal = ""
        for i in range(len(s)):
            j = 0
            while j <= i and j + i < len(s) and s[i-j] == s[i+j]:
                j += 1
            j -= 1

            if j*2 + 1 > len(best_pal):
                best_pal = s[i-j:i+j+1]
            
            if i > 0 and s[i-1] == s[i]:
                while j + 1 <= i and j + i < len(s) and s[i-j-1] == s[i+j]:
                    j += 1
                j -= 1
                if j*2 + 2 > len(best_pal):
                    best_pal = s[i-j-1:i+j+1]
        
        return best_pal

