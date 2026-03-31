import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        sam = []

        heapq.heapify(sam)

        for item in nums:
            if len(sam) < k:
                heapq.heappush(sam,item)
            else:
                heapq.heappush(sam, max(item, heapq.heappop(sam)))
            
            print(sam)
        
        return sam[0]