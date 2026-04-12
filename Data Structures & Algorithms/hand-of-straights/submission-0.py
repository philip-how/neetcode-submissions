import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0 :
            return False

        heapq.heapify(hand)
        counts = {}

        for num in hand:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        while hand:
            smallest_item = heapq.heappop(hand)

            if counts[smallest_item] == 0:
                continue
            
            for i in range(groupSize):
                if smallest_item + i not in counts or counts[smallest_item + i] == 0:
                    return False
                counts[smallest_item + i] -= 1
        
        return True
        