class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            self.time_map[key].append((value, timestamp))
        else:
            self.time_map[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.time_map:
            key_list = self.time_map[key]
            l = 0
            r = len(self.time_map[key]) - 1

            while r - l > 1:
                if key_list[(r+l) // 2][1] > timestamp:
                    r = (r+l) // 2
                else:
                    l = (r+l) // 2
            
            if key_list[r][1] <= timestamp:
                return key_list[r][0]
            if key_list[l][1] <= timestamp:
                return key_list[l][0]

            return ""
        return ""
