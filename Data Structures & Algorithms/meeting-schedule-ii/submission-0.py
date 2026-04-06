"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda inter: inter.start)
        heap = []
        heapq.heapify(heap)

        for i in range(len(intervals)):
            if len(heap) == 0 or heap[0] > intervals[i].start:
                heapq.heappush(heap, intervals[i].end)
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, intervals[i].end)
        
        return len(heap)



        