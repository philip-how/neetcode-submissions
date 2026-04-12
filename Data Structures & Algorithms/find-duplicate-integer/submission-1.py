class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        pointer_1 = 0
        pointer_2 = 0

        while True:
            pointer_1 = nums[pointer_1]
            pointer_2 = nums[nums[pointer_2]]

            if pointer_1 == pointer_2:
                break

        pointer_1 = 0
        while True:
            pointer_1 = nums[pointer_1]
            pointer_2 = nums[pointer_2]

            if pointer_1 == pointer_2:
                return pointer_1
