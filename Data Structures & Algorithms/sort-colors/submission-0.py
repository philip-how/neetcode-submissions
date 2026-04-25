class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red_count = 0
        white_count = 0
        blue_count = 0

        for num in nums:
            if num == 0:
                red_count += 1
            elif num == 1:
                white_count += 1
            elif num == 2:
                blue_count += 1
                
        i = 0
        for j in range(red_count):
            nums[i] = 0
            i += 1
        
        for j in range(white_count):
            nums[i] = 1
            i += 1
        
        for j in range(blue_count):
            nums[i] = 2
            i += 1
        
        