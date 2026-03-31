class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for character in s:
            if character in letters:
                letters[character] += 1
            else:
                letters[character] = 1
            
        for character in t:
            if character in s:
                letters[character] -= 1
            else:
                return False
            
        for letter in letters:
            if letters[letter] != 0:
                return False
            
        return True