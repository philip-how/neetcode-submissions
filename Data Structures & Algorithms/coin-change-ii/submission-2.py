class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # this var stores number of ways to get to each amount
        num_ways = [0] * amount

        for coin in coins:
            if coin > amount:
                continue
            num_ways[coin - 1] += 1
            for value in range(coin, amount):
                num_ways[value] += num_ways[value-coin]
        
        if amount == 0:
            return 1
        return num_ways[-1]
            