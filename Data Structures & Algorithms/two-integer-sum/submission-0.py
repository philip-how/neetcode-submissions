class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        already = {}
        i = 0

        for num in nums:
            if (target - num) in already:
                return [already[target - num], i]
            else:
                already[num] = i
                
            i += 1