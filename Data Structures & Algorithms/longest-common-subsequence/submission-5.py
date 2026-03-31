class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = []
        best = 0
        i = 0
        while i < len(text1):
            rows.append([])
            j = 0
            while j < len(text2):
                if i == 0:
                    if text1[i] == text2[j] or j > 0 and rows[-1][-1] == 1:
                        rows[-1].append(1)
                        if 1 > best:
                            best = 1
                    else:
                        rows[-1].append(0)
                elif j == 0:
                    if text1[i] == text2[j]:
                        rows[-1].append(1)
                        if 1 > best:
                            best = 1
                    else:
                        rows[-1].append(rows[-2][0])
                else:
                    adding_both = rows[-2][j-1]
                    if text1[i] == text2[j]:
                        adding_both += 1
                    rows[-1].append(max(rows[-1][j-1], rows[-2][j], adding_both))
                    if adding_both > best:
                        best = adding_both
                
                j += 1
            
            i += 1
        
        return best
                