class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        not_owning_best = [0] * len(prices)
        owning_best = [0] * len(prices)

        owning_best[0] = -prices[0]

        for i in range(1, len(prices)):
            if i > 2:
                owning_best[i] = max(owning_best[i-1], not_owning_best[i-2] - prices[i])
            else:
                owning_best[i] = max(owning_best[i-1], not_owning_best[0] - prices[i])
            not_owning_best[i] = max(not_owning_best[i-1], owning_best[i-1] + prices[i])
        
        return not_owning_best[-1]