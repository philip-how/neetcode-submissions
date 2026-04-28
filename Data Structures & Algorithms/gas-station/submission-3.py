class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        minimum_running = float("inf")
        min_running_index = -1

        running_gas = []
        total_cost = 0
        prev_total = 0
        for i in range(len(gas)):
            prev_total += gas[i]-cost[i]
            
            if prev_total < minimum_running:
                minimum_running = prev_total
                min_running_index = i
            total_cost += gas[i]-cost[i]
        if total_cost < 0:
            return -1
        return (min_running_index + 1) % len(gas)