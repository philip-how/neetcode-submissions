class Solution:
    def rob(self, nums: List[int]) -> int:
        best_running = []

        for i in range(len(nums)):
            if i == 0:
                best_running.append(nums[0])
            elif i == 1:
                best_running.append(max(nums[0], nums[1]))
            else:
                best_running.append(max(best_running[i-2] + nums[i], best_running[i-1]))
        
        print(best_running)

        return best_running[-1]