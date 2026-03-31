class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1

        lhs_best = height[i]
        rhs_best = height[j]

        water_total = 0

        while i < j - 1:
            if lhs_best < rhs_best:
                i += 1 
                water_total += max(0, min(lhs_best, rhs_best) - height[i])
                lhs_best = max(lhs_best, height[i])
            else:
                j -= 1 
                water_total += max(0, min(lhs_best, rhs_best) - height[j])
                rhs_best = max(rhs_best, height[j])
        
        return water_total
        


