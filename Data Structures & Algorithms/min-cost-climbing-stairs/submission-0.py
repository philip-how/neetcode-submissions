class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = []

        for i in range(len(cost) + 1):
            if i <= 1:
                min_cost.append(0)
            else:
                p1_cost = min_cost[i-1] + cost[i-1]
                p2_cost = min_cost[i-2] + cost[i-2]
                min_cost.append(min(p1_cost, p2_cost))
        
        return min_cost[-1]