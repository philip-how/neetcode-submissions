import heapq

class MedianFinder:

    def __init__(self):
        self.left_heap = []
        self.right_heap = []
        self.middle = None
        heapq.heapify_max(self.left_heap)
        heapq.heapify(self.right_heap)

    def addNum(self, num: int) -> None:
        if self.left_heap is None:
            if self.middle is None:
                self.middle = num
            else:
                heapq.heappush(self.right_heap, num)
                heapq.heappush(self.right_heap, self.middle)
                heapq.heappush_max(self.left_heap, heapq.heappop(self.right_heap))
                self.middle = None
        elif self.middle is None:
            heapq.heappush(self.right_heap, num)
            heapq.heappush_max(self.left_heap, heapq.heappop(self.right_heap))

            self.middle = heapq.heappop_max(self.left_heap)
        else:
            heapq.heappush(self.right_heap, num)
            heapq.heappush(self.right_heap, self.middle)

            heapq.heappush_max(self.left_heap, heapq.heappop(self.right_heap))
            self.middle = None
        

    def findMedian(self) -> float:
        if self.middle is None:
            median = (self.right_heap[0] + self.left_heap[0]) / 2
            return median
        else:
            return self.middle
        

        

