class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        end = 0
        start = 0
        continuous_sum = 0
        best_sum = float("-inf")
        while end < len(nums):
            continuous_sum += nums[end]
            if continuous_sum > best_sum:
                best_sum = continuous_sum
            
            if continuous_sum <= 0:
                start = end + 1
                continuous_sum = 0

            end += 1
        
        return best_sum