class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        nums_already = {}
        output = []
        output_dict = {}

        while i < len(nums):
            if nums[i] in nums_already and nums_already[nums[i]] >= 3:
                i += 1
                continue
            j = i + 1
            while j < len(nums):
                if -nums[i]-nums[j] in nums_already and tuple(sorted([nums[i], nums[j], -nums[i]-nums[j]])) not in output_dict:
                    output.append(sorted([-nums[i]-nums[j], nums[i], nums[j]]))
                    output_dict[tuple(sorted([nums[i], nums[j], -nums[i]-nums[j]]))] = True
                j += 1
            if nums[i] in nums_already:
                nums_already[nums[i]] += 1
            else:
                nums_already[nums[i]] = True
            i += 1
        
        return output