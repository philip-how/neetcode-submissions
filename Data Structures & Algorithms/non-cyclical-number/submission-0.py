class Solution:
    def isHappy(self, n: int) -> bool:
        alr_done = {}
        while True:
            new_n = 0
            while n != 0:
                new_n = new_n + (n % 10) ** 2
                n = n // 10
            n = new_n
            if n in alr_done:
                return False
            else:
                alr_done[n] = True
            if n == 1:
                return True 