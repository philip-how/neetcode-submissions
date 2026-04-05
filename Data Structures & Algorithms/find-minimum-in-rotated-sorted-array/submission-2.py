class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while r - l > 1:
            if nums[l] > nums[r]:
                l = l + (r-l)//2
            elif nums[l] < nums[r]:
                movement = (r-l)//2
                r = r - movement
                l = max(l - movement, 0)
            
        
        return min(nums[l], nums[r])
