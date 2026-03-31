class Solution:
    def isPalindrome(self, s: str) -> bool:
        simplified = []

        for character in s:
            if character.isalnum():
                simplified.append(character.lower())
            
        i = 0
        while i < (len(simplified) / 2):
            if simplified[i] != simplified[-1-i]:
                print(i, simplified)
                return False
            i += 1
        
        return True