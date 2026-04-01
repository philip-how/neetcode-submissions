class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        prevs = []
        i = 0
        overall_best = 1
        while i < len(nums):
            if i == 0:
                prevs.append((nums[0], 1))
                i += 1
                continue
            j = 0
            best = 1
            while j < i:
                if prevs[j][0] < nums[i]:
                    best = max(best, prevs[j][1] + 1)
                j += 1
            overall_best = max(best, overall_best)
            prevs.append((nums[i], best))
            i += 1
        
        return overall_best
