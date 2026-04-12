class Solution:
    def decodeInnerString(self, string, brackets, start_index, end_index):
        decoded_string = []
        i = start_index
        while i < end_index:
            if string[i] in self.integers:
                integer = ""
                while string[i] in self.integers:
                    integer += string[i]
                    i += 1
                multiplier = int(integer)

                inner_string = self.decodeInnerString(string, brackets, i + 1, brackets[i])
                for j in range(multiplier):
                    decoded_string.append(inner_string)
                i = brackets[i]
            else:
                decoded_string.append(string[i])
            i += 1
        
        return "".join(decoded_string)



            

    def decodeString(self, s: str) -> str:
        self.integers = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        end_brackets = {}
        left_bracket_stack = []
        for i, char in enumerate(s):
            if char == "[":
                left_bracket_stack.append(i)
            elif char == "]":
                end_brackets[left_bracket_stack.pop()] = i
        

        return self.decodeInnerString(s, end_brackets, 0, len(s))