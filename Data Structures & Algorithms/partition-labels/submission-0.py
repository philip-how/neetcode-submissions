class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        earliest_spot = {}
        latest_spot = {}

        for i, char in enumerate(s):
            if char not in earliest_spot:
                earliest_spot[char] = i
            latest_spot[char] = i
        

        earliest_pos = [0] * len(s)

        i = len(s) - 1
        while i >= 0:
            if i == len(s) - 1:
                earliest_pos[i] = earliest_spot[s[i]]
            else:
                earliest_pos[i] = min(earliest_pos[i+1], earliest_spot[s[i]])
            
            i -= 1
        
        i = 1
        prev = earliest_pos[0]
        current_group_size = 1
        current_group_latest = latest_spot[s[0]]
        groups = []
        while i < len(s):
            if earliest_pos[i] != prev and i > current_group_latest:
                prev = earliest_pos[i]
                groups.append(current_group_size)
                current_group_size = 1
                current_group_latest = latest_spot[s[i]]
            else:
                current_group_size += 1
                current_group_latest = max(current_group_latest, latest_spot[s[i]])
            i += 1
        
        groups.append(current_group_size)

        return groups