class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coin_amounts = [float("inf")] * (amount + 1)
        coin_amounts[0] = 0

        for i in range(len(coins)):
            j = coins[i]
            while j <= amount:
                if 1 + coin_amounts[j-coins[i]] < coin_amounts[j]:
                    coin_amounts[j] = 1 + coin_amounts[j-coins[i]]
                j += 1
            print(coin_amounts)
        if coin_amounts[-1] != float("inf"):
            return coin_amounts[-1]
        return -1