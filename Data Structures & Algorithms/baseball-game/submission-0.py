class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for operation in operations:
            if operation == "+":
                scores.append(scores[-2] + scores[-1])
            elif operation == "D":
                scores.append(2 * scores[-1])
            elif operation == "C":
                scores.pop()
            else:
                scores.append(int(operation))
        
        total = 0
        for score in scores:
            total += score
        
        return total