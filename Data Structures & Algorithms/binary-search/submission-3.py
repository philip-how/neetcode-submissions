class Solution:
    def search(self, nums: List[int], target: int) -> int:
        upper_bound = len(nums) - 1
        lower_bound = 0

        while upper_bound - lower_bound > 1:
            if nums[upper_bound - (upper_bound - lower_bound) // 2] > target:
                upper_bound = upper_bound - (upper_bound - lower_bound) // 2
            elif nums[upper_bound - (upper_bound - lower_bound) // 2] == target:
                return upper_bound - (upper_bound - lower_bound) // 2
            else:
                lower_bound = (upper_bound - lower_bound) // 2 + lower_bound
        
        if nums[lower_bound] == target:
            return lower_bound
        elif nums[upper_bound] == target:
            return upper_bound
        
        return -1
            