import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heapq.heapify_max(nums)

        # i = 0
        # while i < k - 1:
        #     heapq.heappop_max(nums)
        #     i += 1

        return heapq.nlargest(k, nums)[-1]