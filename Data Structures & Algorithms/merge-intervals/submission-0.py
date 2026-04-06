class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda interval: interval[0])

        latest_end = -1
        latest_end_start = -1

        output = []

        for interval in intervals:
            if interval[0] <= latest_end:
                latest_end = max(interval[1], latest_end)
            else:
                if latest_end != -1:
                    output.append([latest_end_start, latest_end])
                latest_end_start = interval[0]
                latest_end = interval[1]
        
        if latest_end != -1:
            output.append([latest_end_start, latest_end])
        
        return output