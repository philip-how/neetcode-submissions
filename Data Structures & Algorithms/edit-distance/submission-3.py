class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        prev = []
        for j in range(len(word1) + 1):
            prev.append(j)
        curr = [max(len(word1), len(word2))]
        
        for i in range(1, len(word2) + 1):
            curr = [i]
            for j in range(1, len(word1) + 1):
                options = [curr[j-1] + 1, prev[j] + 1]
                if word2[i-1] == word1[j-1]:
                    options.append(prev[j-1])
                else:
                    options.append(prev[j-1] + 1)
                
                curr.append(min(options))
            prev = curr
        
        return curr[-1]
