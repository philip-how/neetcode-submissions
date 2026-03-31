class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for number in nums:
            if number in dict:
                return True
            else:
                dict[number] = True

        return False
        