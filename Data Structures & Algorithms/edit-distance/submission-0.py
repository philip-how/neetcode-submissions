class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = []
        for i in range(len(word2) + 1):
            memo.append([])
            for j in range(len(word1) + 1):
                memo[-1].append(0)
        
        for j in range(len(word1) + 1):
            memo[0][j] = j
        
        for i in range(len(word2) + 1):
            memo[i][0] = i
        
        for i in range(1, len(word2) + 1):
            for j in range(1, len(word1) + 1):
                options = [memo[i][j-1] + 1, memo[i-1][j] + 1]
                if word2[i-1] == word1[j-1]:
                    options.append(memo[i-1][j-1])
                else:
                    options.append(memo[i-1][j-1] + 1)
                
                memo[i][j] = min(options)
        
        return memo[-1][-1]
