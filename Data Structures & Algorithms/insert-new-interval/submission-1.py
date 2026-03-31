class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        lowest_conflicting_start = newInterval[0]
        highest_conflicting_end = newInterval[1]

        real_soln = []

        soln_added = False
        soln_index = -1

        i = 0
        while i < len(intervals):
            if intervals[i][1] >= newInterval[0] and intervals[i][0] <= newInterval[1]:
                lowest_conflicting_start = min(lowest_conflicting_start, intervals[i][0])
                highest_conflicting_end = max(highest_conflicting_end, intervals[i][1])
            else: 
                if not soln_added and lowest_conflicting_start < intervals[i][0]:
                    soln_added = True
                    soln_index = len(real_soln)
                    real_soln.append([lowest_conflicting_start, 0])
                real_soln.append(intervals[i])
            i += 1
        
        if not soln_added:
            soln_added = True
            soln_index = len(real_soln)
            real_soln.append([lowest_conflicting_start, 0])
        
        real_soln[soln_index][1] = highest_conflicting_end

        return real_soln


            