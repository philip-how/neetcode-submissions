class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest_buy_so_far = 200
        best_combo_so_far = 0

        for price in prices:
            if price - cheapest_buy_so_far > best_combo_so_far:
                best_combo_so_far = price - cheapest_buy_so_far
            if price < cheapest_buy_so_far:
                cheapest_buy_so_far = price
        
        return best_combo_so_far