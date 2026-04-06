class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda ls: ls[1])
        last_useful_end = -50001
        
        count = 0

        i = 0
        while i < len(intervals):
            if intervals[i][0] >= last_useful_end:
                count += 1
                last_useful_end = intervals[i][1]
            i += 1
        
        return len(intervals) - count