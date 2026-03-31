class Solution:
    def minWindow(self, s: str, t: str) -> str:
        found = 0
        needed = {}
        for char in t:
            if char not in needed:
                needed[char] = 0
                found += 1
            needed[char] += 1
        
        best_length = float("inf")
        best_string = ""
        i = -1
        window_start = 0
        while i < len(s):
            i += 1
            if i == len(s):
                break
            
            if s[i] in needed:
                needed[s[i]] -= 1
                if needed[s[i]] == 0:
                    found -= 1

            
            while window_start < len(s) and (s[window_start] not in needed or needed[s[window_start]] < 0):
                if s[window_start] in needed:
                    needed[s[window_start]] += 1
                window_start += 1
            
            if found == 0:
                if i - window_start + 1 < best_length:
                    best_string = s[window_start:i+1]
                    
                best_length = min(best_length, i - window_start + 1)
            
            
        
        return best_string


        
