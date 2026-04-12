class Solution:
    def startingFrom(self, digits, index, combinations, mapping, running_string):
        if index == len(digits):
            if len(running_string) > 0:
                combinations.append("".join(running_string))
            return
        
        for char in mapping[digits[index]]:
            running_string.append(char)
            self.startingFrom(digits, index + 1, combinations, mapping, running_string)
            running_string.pop()
        
        return
        

    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        combinations = []

        self.startingFrom(digits, 0, combinations, mapping, [])

        return combinations