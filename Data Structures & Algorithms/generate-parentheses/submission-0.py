class Solution:
    def continueGeneration(self, string, right_stack, left_stack):
        if right_stack == 0 and left_stack == 0:
            if len(string) > 0:
                self.strings.append("".join(string))
            return
        
        if left_stack > 0:
            string.append("(")
            self.continueGeneration(string, right_stack + 1, left_stack - 1)
            string.pop()
        
        if right_stack > 0:
            string.append(")")
            self.continueGeneration(string, right_stack - 1, left_stack)
            string.pop()
        
        return

    def generateParenthesis(self, n: int) -> List[str]:
        self.strings = []
        # this is the same as all 

        # (()())
        self.continueGeneration([], 0, n)

        return self.strings