class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort intervals descending order based on the end points
        # best to remove interval
        
        intervals.sort(key=lambda x: x[1])
        k = -inf
        res = 0
        for x, y in intervals:
            if x >= k:
                k = y
            else:
                res += 1

        return res