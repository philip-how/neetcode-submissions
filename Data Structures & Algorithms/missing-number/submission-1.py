class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_sum = 0
        real_sum = 0
        i = 0
        while i < len(nums):
            total_sum += nums[i]
            real_sum += i
            i += 1
        
        real_sum += i
        
        return real_sum - total_sum