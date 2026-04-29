class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        nums_sum = sum(nums)
        if abs(target) > nums_sum:
            return 0

        ways_to_reach = [0] * (2 * nums_sum + 1)

        ways_to_reach[nums_sum] = 1

        for num in nums:
            new_ways_to_reach = []
            i = 0
            while i < (2 * nums_sum + 1):
                new_ways_to_reach.append(0)
                if i >= num:
                    new_ways_to_reach[i] += ways_to_reach[i-num]
                if i < len(ways_to_reach) - num:
                    new_ways_to_reach[i] += ways_to_reach[i+num]
                i += 1
            
            ways_to_reach = new_ways_to_reach
        
        return ways_to_reach[nums_sum + target]