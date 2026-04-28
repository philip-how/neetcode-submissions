class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        minimum_running = float("inf")
        min_running_index = -1

        running_gas = []
        total_cost = 0
        for i in range(len(gas)):
            if len(running_gas) == 0:
                running_gas.append(gas[i]-cost[i])
            else:
                running_gas.append(running_gas[-1] + gas[i]-cost[i])
            if running_gas[-1] < minimum_running:
                minimum_running = running_gas[-1]
                min_running_index = i
            total_cost += gas[i]-cost[i]
        if total_cost < 0:
            return -1
        return (min_running_index + 1) % len(gas)