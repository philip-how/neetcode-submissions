class Solution:
    def all_possibilities(self, so_far_sum, so_far, nums, target, index):
        if target - so_far_sum - nums[index] < 0:
            return 
        if target - so_far_sum - nums[index] == 0:
            so_far.append(nums[index])
            self.solns.append(so_far.copy())
            so_far.pop()
            return
        so_far.append(nums[index])
        so_far_sum += nums[index]
        for alt in range(index, len(nums)):
            self.all_possibilities(so_far_sum, so_far, nums, target, alt)
        so_far.pop()

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.solns = []
        for choice in range(len(nums)):
            self.all_possibilities(0, [], nums, target, choice)
        return self.solns
        