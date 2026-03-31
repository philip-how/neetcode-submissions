class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        not_beaten = []
        output_ls = [0] * len(temperatures)

        i = 0
        while i < len(temperatures):
            while len(not_beaten) != 0 and temperatures[i] > temperatures[not_beaten[-1]]:
                output_ls[not_beaten[-1]] = i - not_beaten[-1]
                not_beaten.pop()
            
            not_beaten.append(i)
            i += 1
        
        return output_ls