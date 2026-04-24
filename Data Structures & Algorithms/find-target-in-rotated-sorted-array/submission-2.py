class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # first, find the minimum
        l = 0
        r = len(nums) - 1

        while nums[r] < nums[l] and r - l > 1:
            mid = l + (r-l)//2
            if nums[l] > nums[mid]:
                r = mid
            else:
                l = mid
        
        if nums[l] < nums[r]:
            minimum = l
        else:
            minimum = r
        
        l = 0
        r = len(nums) - 1

        while r - l > 1:
            mid = l + (r-l)//2
            if nums[(mid+minimum)%len(nums)] > target:
                r = mid
            else:
                l = mid
        
        if nums[(l+minimum)%len(nums)] == target:
            return (l+minimum)%len(nums)
        elif nums[(r+minimum)%len(nums)] == target:
            return (r+minimum)%len(nums)
        else:
            return -1