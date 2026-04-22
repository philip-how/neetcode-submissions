class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        total = 0
        for operation in operations:
            if operation == "+":
                scores.append(scores[-2] + scores[-1])
                total += scores[-1]
            elif operation == "D":
                scores.append(2 * scores[-1])
                total += scores[-1]
            elif operation == "C":
                total -= scores.pop()
            else:
                scores.append(int(operation))
                total += scores[-1]
        
        return total