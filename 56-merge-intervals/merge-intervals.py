class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals based on start number
        # for each interval,  if start > previous end, add to res
        # else: merge with previous interval

        intervals.sort(key=lambda x: x[0])
        res = []
        prev_start, prev_end = intervals[0]

        for start, end in intervals:
            if start > prev_end:
                res.append([prev_start, prev_end])
                prev_start, prev_end = start, end
            else:
                prev_end = max(prev_end, end)
        
        res.append([prev_start, prev_end])

        return res

