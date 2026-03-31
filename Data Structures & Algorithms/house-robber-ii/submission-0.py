class Solution:
    def rob(self, nums: List[int]) -> int:
        best_running = []
        best_running_no_first = []

        for i in range(len(nums)):
            if i == 0:
                best_running.append(nums[0])
                best_running_no_first.append(0)
            elif i == 1:
                best_running.append(max(nums[0], nums[1]))
                best_running_no_first.append(nums[1])
            else:
                if i != len(nums) - 1:
                    best_running.append(max(best_running[i-2] + nums[i], best_running[i-1]))
                best_running_no_first.append(max(best_running_no_first[i-2] + nums[i], best_running_no_first[i-1]))
        
        print(best_running)
        print(best_running_no_first)

        return max(best_running[-1], best_running_no_first[-1])