class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        existed = {}

        for num in nums:
            if num in existed:
                existed[num] += 1
            else:
                existed[num] = 1

        reversed_pairs = []
        for pair in existed.items():
            first, second = pair
            reversed_pairs.append([second, first])
        
        real_reversed_pairs = sorted(reversed_pairs, reverse=True)

        output = []
        for i in range(k):
            output.append(real_reversed_pairs[i][1])
        
        return output

        

                

        