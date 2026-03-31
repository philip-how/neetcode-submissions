import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pq = []
        heapq.heapify(self.pq)

        for num in nums:
            heapq.heappush(self.pq, -num)

    def add(self, val: int) -> int:
        heapq.heappush(self.pq, -val)

        return - heapq.nsmallest(self.k, self.pq)[-1]
        
