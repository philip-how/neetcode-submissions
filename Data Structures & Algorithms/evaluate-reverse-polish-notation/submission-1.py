class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ls = []
        OPERATORS = ["-", "/", "*", "+"]

        for token in tokens:
            if token in OPERATORS:
                num2 = ls.pop()
                num1 = ls.pop()
                ls.append(Solution.operator(num1, num2, token))
            else:
                ls.append(int(token))
        
        return ls[0]

    def operator(num1, num2, op):
        print(num1, op, num2)

        if op == "-":
            return num1 - num2
        elif op == "/":
            return int(num1 / num2)
        elif op == "*":
            return num1 * num2
        else:
            return num1 + num2
        