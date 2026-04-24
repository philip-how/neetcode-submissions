class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            add_me = True
            while asteroid < 0 and len(stack) > 0 and stack[-1] > 0 and stack[-1] < -asteroid:
                stack.pop()
            
            if asteroid < 0 and len(stack) > 0 and stack[-1] > 0 and stack[-1] == -asteroid:
                stack.pop()
                add_me = False

            if asteroid < 0 and len(stack) > 0 and stack[-1] > 0 and stack[-1] > -asteroid:
                add_me = False
            
            if add_me:
                stack.append(asteroid)

        return stack