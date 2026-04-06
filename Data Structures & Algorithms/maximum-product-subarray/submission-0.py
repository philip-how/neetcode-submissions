class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pos_current = None
        neg_current = None

        overall_best = float("-inf")

        i = 0
        while i < len(nums):
            if pos_current is None:
                pos_calc = 1
            else:
                pos_calc = pos_current
            if neg_current is None:
                neg_calc = 1
            else:
                neg_calc = neg_current
            
            neg_current = min(neg_calc * nums[i], pos_calc * nums[i])
            pos_current = max(neg_calc * nums[i], pos_calc * nums[i])

            if pos_current > overall_best:
                overall_best = pos_current

            if pos_current < 1:
                pos_current = 1
            i += 1
        
        return overall_best

            
