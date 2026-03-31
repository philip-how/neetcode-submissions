class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        output = []

        anagrams = {}

        first_26_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]


        for string in strs:
            match_found = False
            string_number = 1

            for character in string:
                string_number *= first_26_primes[ord(character) - ord('a')]

            if string_number in anagrams:
                output[anagrams[string_number]].append(string)
            else:
                output.append([string])
                anagrams[string_number] = len(output) - 1

        return output

                

        