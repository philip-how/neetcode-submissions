class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        characters_needed = {}
        for character in s1:
            if character in characters_needed:
                characters_needed[character] += 1
            else:
                characters_needed[character] = 1

        away_from_correctness = len(s1)

        start_pointer = 0
        i = 0
        while i < len(s2):
            if s2[i] in characters_needed:
                characters_needed[s2[i]] -= 1
                if characters_needed[s2[i]] >= 0:
                    away_from_correctness -= 1
                else:
                    away_from_correctness += 1
            
            if i >= len(s1):
                if s2[start_pointer] in characters_needed:
                    characters_needed[s2[start_pointer]] += 1
                    if characters_needed[s2[start_pointer]] <= 0:
                        away_from_correctness -= 1
                    else:
                        away_from_correctness += 1
                start_pointer += 1
            
            if away_from_correctness == 0:
                print(start_pointer, i, characters_needed)
                return True
            
            i += 1
        
        return False

