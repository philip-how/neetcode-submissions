import heapq

class Solution:
    def getRealBest(self, heap_best, count_in):
        if len(heap_best) == 0:
            return 0
        while count_in[heap_best[0][1]] != -heap_best[0][0]:
            heapq.heappop(heap_best)
            if len(heap_best) == 0:
                return 0
        
        return -heap_best[0][0]

    def characterReplacement(self, s: str, k: int) -> int:
        end_window = 0
        start_window = 0
        count_in = {}
        heap_best = []
        heapq.heapify(heap_best)

        best_score = 0

        while start_window < len(s):
            if s[start_window] in count_in:
                count_in[s[start_window]] += 1
                heapq.heappush(heap_best, (-count_in[s[start_window]], s[start_window]))
            else:
                count_in[s[start_window]] = 1
                heapq.heappush(heap_best, (-count_in[s[start_window]], s[start_window]))

            while start_window - end_window >= self.getRealBest(heap_best, count_in) + k:
                count_in[s[end_window]] -= 1
                heapq.heappush(heap_best, (-count_in[s[end_window]], s[end_window]))
                end_window += 1
            
            print(start_window, end_window)
            
            best_score = max(best_score, start_window - end_window + 1)
            
            start_window += 1
        
        return best_score
