class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums2 = []
        nums2.extend(nums)
        nums2.extend(nums)
        return nums2
