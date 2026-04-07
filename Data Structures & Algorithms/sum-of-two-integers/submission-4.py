import math
class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a < 0 and b < 0:
            return -int(math.log2(2**(-a) * 2**(-b)))
        return int(math.log2(2**a * 2**b))