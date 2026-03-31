class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable_max = 0

        for i in range(len(nums)):
            if reachable_max < i:
                return False
            if nums[i] + i > reachable_max:
                reachable_max = nums[i] + i
        
        return True