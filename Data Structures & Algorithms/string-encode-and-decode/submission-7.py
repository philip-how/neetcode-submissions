class Solution:

    def encode(self, strs: List[str]) -> str:

        output_string = ""

        for string in strs:
            if len(string) < 10:
                output_string += "00" + str(len(string))
                print("00" + str(len(string)))
            elif len(string) < 100:
                output_string += "0" + str(len(string))
                print("0" + str(len(string)))
            else:
                output_string += str(len(string))
                print(str(len(string)))
        
        output_string += "#"

        new_output_string = output_string + "".join(strs)

        print(new_output_string)

        return new_output_string

    def decode(self, s: str) -> List[str]:

        string_lengths = []

        i = 0
        while s[i] != "#":
            string_lengths.append(int(s[i:i+3]))
            i += 3

        i += 1

        strs = []

        for length in string_lengths:
            strs.append(s[i:i + length])

            i += length

        return strs


