class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals based on start times
        # initialize res
        # add the first interval to res
        # iterate the subsequence interval in intervals
        # if start < previous: merge by getting the earliest sttart and latest end
        
        if len(intervals) == 1:
            return intervals
        
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            prev_start, prev_end = res[-1]

            if start <= prev_end:
                new_end = max(prev_end, end)
                res[-1][1] = new_end
            else:
                res.append([start, end])
        
        return res