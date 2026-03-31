class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        found_numbers = {}
        number_counters = {}
        best = 0

        for number in nums:
            if number in found_numbers:
                continue
            if number + 1 in found_numbers and number - 1 in found_numbers:
                looking_for = found_numbers[number + 1]
                while type(number_counters[looking_for]) != int:
                    looking_for = int(number_counters[looking_for])
                    
                number_counters[looking_for] += 1
                if number_counters[looking_for] > best:
                    best = number_counters[looking_for]

                plus_one_looking_for = looking_for

                looking_for = found_numbers[number - 1]
                while type(number_counters[looking_for]) != int:
                    looking_for = int(number_counters[looking_for])

                number_counters[plus_one_looking_for] += number_counters[looking_for]
                if number_counters[plus_one_looking_for] > best:
                    best = number_counters[plus_one_looking_for]
                    
                number_counters[looking_for] = str(found_numbers[number + 1])

                found_numbers[number] = found_numbers[number + 1]
            elif number + 1 in found_numbers:
                looking_for = found_numbers[number + 1]
                while type(number_counters[looking_for]) != int:
                    looking_for = int(number_counters[looking_for])
                
                number_counters[looking_for] += 1

                if number_counters[looking_for] > best:
                    best = number_counters[looking_for]
                
                found_numbers[number] = found_numbers[number + 1]

                
            elif number - 1 in found_numbers:
                looking_for = found_numbers[number - 1]
                while type(number_counters[looking_for]) != int:
                    looking_for = int(number_counters[looking_for])
                    
                number_counters[looking_for] += 1

                if number_counters[looking_for] > best:
                    best = number_counters[looking_for]
                
                found_numbers[number] = found_numbers[number - 1]
            else:
                found_numbers[number] = number
                number_counters[number] = 1

                if best == 0:
                    best = 1
        
        return best
