class Solution:
    def numDecodings(self, s: str) -> int:
        running_bad_ending = []
        running_one_ending = []

        for i in range(len(s)):
            if i == 0:
                running_bad_ending.append(0)
                running_one_ending.append(1)
                if s[i] == "0":
                    return 0
                continue
            
            if s[i] == "0":
                running_one_ending.append(0)
                if int(s[i-1]) <= 2: 
                    running_bad_ending.append(running_one_ending[i-1])
                else:
                    return 0
            elif s[i-1] == "1" or (s[i-1] == "2" and int(s[i]) <= 6):
                running_one_ending.append(running_one_ending[i-1] + running_bad_ending[i-1])
                running_bad_ending.append(running_one_ending[i-1])
            else:
                running_bad_ending.append(0)
                running_one_ending.append(running_one_ending[i-1] + running_bad_ending[i-1])
        
        print(running_bad_ending)
        print(running_one_ending)

        return running_bad_ending[-1] + running_one_ending[-1]
