class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        reachable = []
        for i in range(len(s)):
            reachable.append([])
            for j in range(len(t)):
                reachable[-1].append(0)

        for i in range(len(s)):
            if s[i] == t[0]:
                reachable[i][0] = 1
            for j in range(len(t)):
                if i > 0:
                    reachable[i][j] += reachable[i-1][j]
                    if j > 0 and s[i] == t[j]:
                        reachable[i][j] += reachable[i-1][j - 1]
        
        return reachable[-1][-1]
        