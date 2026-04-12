class Solution:
    def getAllChoices(self, nums, chosen, curr):
        if len(curr) == len(nums):
            self.combos.append(curr[:])
        
        for i in range(len(nums)):
            if chosen[i]:
                continue
            chosen[i] = True
            curr.append(nums[i])
            self.getAllChoices(nums, chosen, curr)
            curr.pop()
            chosen[i] = False

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.combos = []
        chosen = [False] * len(nums)

        self.getAllChoices(nums, chosen, [])

        return self.combos
        