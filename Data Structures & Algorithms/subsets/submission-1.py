class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        people = [0] * len(nums)
        return_val = []
        j = 0
        while people is not None:
            this_one = []
            i = 0
            while i < len(nums):
                if people[i] == 1:
                    this_one.append(nums[i])
                i += 1
            
            return_val.append(this_one)
            if self.increment_people(people):
                break
            j += 1
        
        return return_val


    def increment_people(self, people):
        i = len(people) - 1
        while i >= 0 and people[i] != 0:
            people[i] = 0
            i -= 1
        if i == -1:
            return True
        people[i] = 1
        return False