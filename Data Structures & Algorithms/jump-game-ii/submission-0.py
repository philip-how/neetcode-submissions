class Solution:
    def jump(self, nums: List[int]) -> int:
        
        curr_jump_count = 0

        max_reachable = 0
        next_max_reachable = -100

        i = 0
        while i < len(nums):
            next_max_reachable = max(next_max_reachable, i+nums[i])
            if max_reachable == i and i != len(nums) - 1:
                curr_jump_count += 1
                max_reachable = next_max_reachable
            i += 1

        return curr_jump_count
