class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        prev = [False] * (len(s2) + 1)
        curr = [False] * (len(s2) + 1)
        curr[0] = True

        if len(s1) + len(s2) != len(s3):
            return False

        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                curr[j] = curr[j] or i > 0 and prev[j] and s1[i-1] == s3[i+j-1]
                curr[j] = curr[j] or j > 0 and curr[j-1] and s2[j-1] == s3[i+j-1]
            prev = curr
            curr = [False] * (len(s2) + 1)

        return prev[-1]