class Solution:
    def find_all_solns(self, start, index, combos):
        if index >= len(combos):
            self.solns.append(start.copy())
            return

        for i in range(combos[index][1] + 1):
            self.find_all_solns(start, index + 1, combos)
            start.append(combos[index][0])

        for i in range(combos[index][1] + 1):
            start.pop()
        

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        numbers = {}
        for num in nums:
            if num in numbers:
                numbers[num] += 1
            else:
                numbers[num] = 1
        
        combos = []
        for key, value in numbers.items():
            combos.append([key, value])

        self.solns = []
        self.find_all_solns([], 0, combos)
        return self.solns