class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        latest_spot = {}

        for i, char in enumerate(s):
            latest_spot[char] = i
        
        i = 1
        current_group_size = 1
        current_group_latest = latest_spot[s[0]]
        groups = []
        while i < len(s):
            if i > current_group_latest:
                groups.append(current_group_size)
                current_group_size = 1
                current_group_latest = latest_spot[s[i]]
            else:
                current_group_size += 1
                current_group_latest = max(current_group_latest, latest_spot[s[i]])
            i += 1
        
        groups.append(current_group_size)

        return groups