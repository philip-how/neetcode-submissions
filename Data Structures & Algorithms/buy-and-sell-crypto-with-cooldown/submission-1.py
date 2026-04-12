class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        owning_best_prev = -prices[0]
        not_owning_best_prev = 0
        not_owning_best_2prev = 0

        for i in range(1, len(prices)):
            if i > 2:
                new_owning_best = max(owning_best_prev, not_owning_best_2prev - prices[i])
            else:
                new_owning_best = max(owning_best_prev, 0 - prices[i])
            new_not_owning_best = max(not_owning_best_prev, owning_best_prev + prices[i])

            not_owning_best_2prev = not_owning_best_prev
            not_owning_best_prev = new_not_owning_best
            owning_best_prev = new_owning_best

            print(not_owning_best_2prev, not_owning_best_prev, owning_best_prev)
        
        return not_owning_best_prev