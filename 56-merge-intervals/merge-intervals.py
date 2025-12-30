class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        intervals.sort()
        res = [intervals[0]]
        for curr_start, curr_end in intervals[1:]:
            prev_start, prev_end = res[-1]
            if prev_end >= curr_start:
                res[-1] = [min(curr_start, prev_start), max(curr_end, prev_end)]
            else:
                res.append([curr_start, curr_end])
        
        return res