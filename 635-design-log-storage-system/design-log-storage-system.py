class LogSystem:

    def __init__(self):
        self.logs = []

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append((timestamp, id))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        k = 19
        if granularity == "Minute":
            k = 16
        elif granularity == "Hour":
            k = 13
        elif granularity == "Day":
            k = 10
        elif granularity == "Month":
            k = 7
        elif granularity == "Year":
            k = 4
        
        res = []
        for timestamp, id in self.logs:
            if start[:k] <= timestamp[:k] <= end[:k]:
                res.append(id)
        return res



# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)