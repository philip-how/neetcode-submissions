class Solution:
    def climbStairs(self, n: int) -> int:
        soln_so_far = []

        for i in range(n):
            if i == 0:
                num = 1
            elif i == 1:
                num = 2
            else:
                num = soln_so_far[-2] + soln_so_far[-1]

            soln_so_far.append(num)
        
        print(soln_so_far)
        return soln_so_far[-1]