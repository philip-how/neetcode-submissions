class Solution:
    #Idea: stack for fastest to make it, 
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        new_list = []
        i = 0
        while i < len(position):
            new_list.append((position[i], speed[i]))
            i += 1
        
        new_list.sort()

        groups = 0
        max_time_reached = 0
        while new_list:
            pos, spd = new_list.pop()

            distance_away = (target - pos)

            if distance_away / spd > max_time_reached:
                groups += 1
                max_time_reached = distance_away / spd
        
        return groups

