class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        can_put_space_after = [True]
        max_len = 0
        for word in wordDict:
            max_len = max(max_len, len(word))

        wordDict = set(wordDict)

        i = 0
        while i < len(s):
            found_possibility = False
            j = max(i-max_len, 0)
            while j <= i:
                if can_put_space_after[j] and s[j:i+1] in wordDict:
                    found_possibility = True
                j += 1
            
            can_put_space_after.append(found_possibility)
            i += 1
        return can_put_space_after[-1]