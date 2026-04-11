class Solution:
    def convertToInt(self, char: str):
        if char == "0":
            return 0
        if char == "1":
            return 1
        if char == "2":
            return 2
        if char == "3":
            return 3
        if char == "4":
            return 4
        if char == "5":
            return 5
        if char == "6":
            return 6
        if char == "7":
            return 7
        if char == "8":
            return 8
        if char == "9":
            return 9

    def multiply(self, num1: str, num2: str) -> str:
        output = 0
        for i, char in enumerate(num1[::-1]):
            int1 = self.convertToInt(char)
            for j, char2 in enumerate(num2[::-1]):
                int2 = self.convertToInt(char2)
                output += int1 * int2 * (10 ** (i+j))
        
        return str(output)
