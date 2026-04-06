class Solution:
    def countBits(self, n: int) -> List[int]:
        ls = []
        for i in range(n + 1):
            count = 0
            for char in bin(i):
                if char == "b":
                    continue
                count += int(char)
            ls.append(count)

        return ls