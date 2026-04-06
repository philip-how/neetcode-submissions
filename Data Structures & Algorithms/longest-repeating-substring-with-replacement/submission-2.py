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
        true_best_freq = 0
        

        best_score = 0

        while start_window < len(s):
            if s[start_window] in count_in:
                count_in[s[start_window]] += 1
                if count_in[s[start_window]] > true_best_freq:
                    true_best_freq = count_in[s[start_window]]
            else:
                count_in[s[start_window]] = 1
                if count_in[s[start_window]] > true_best_freq:
                    true_best_freq = count_in[s[start_window]]

            while start_window - end_window >= true_best_freq + k:
                count_in[s[end_window]] -= 1
                end_window += 1
            
            best_score = max(best_score, start_window - end_window + 1)
            
            start_window += 1
        
        return best_score
