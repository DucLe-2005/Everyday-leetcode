class TimeMap:

    def __init__(self):
        self.keyMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyMap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        values = self.keyMap[key]
        l, r = 0, len(values)
        while l < r:
            m = (l + r) // 2

            if values[m][0] <= timestamp: # timestamp at l is valid, try l + 1
                l = m + 1
            else:
                r = m

        return values[l-1][1] if l > 0 else ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)