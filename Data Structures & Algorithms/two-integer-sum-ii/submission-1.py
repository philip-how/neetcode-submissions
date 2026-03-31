class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while True:
            print(i, j)
            while numbers[i] + numbers[j] < target:
                i += 1
            
            if numbers[i] + numbers[j] == target and numbers[i] != numbers[j]:
                return [i + 1, j + 1]
            
            j -= 1

            