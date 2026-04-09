import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        epic_heap = []
        heapq.heapify_max(epic_heap)

        start_window = 0
        end_window = 0
        while end_window < k - 1:
            heapq.heappush_max(epic_heap, (nums[end_window], end_window))
            end_window += 1

        output = []
        
        while end_window < len(nums):
            heapq.heappush_max(epic_heap, (nums[end_window], end_window))
            while epic_heap[0][1] < start_window:
                heapq.heappop_max(epic_heap)
            output.append(epic_heap[0][0])
            start_window += 1
            end_window += 1
        
        return output