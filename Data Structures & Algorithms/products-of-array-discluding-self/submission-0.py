class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = 1
        zero_result = False
        two_zero_results = False

        for num in nums:
            if num == 0:
                if zero_result:
                    two_zero_results = True
                else:
                    zero_result = True
            else:
                result *= num

        output = []

        for num in nums:
            if two_zero_results or (zero_result and num != 0):
                output.append(0) 
            elif zero_result and num == 0:
                output.append(result)
            else:
                output.append(int(result / num))

        return output


        