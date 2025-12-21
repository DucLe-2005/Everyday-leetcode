class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. sort the intervals
        # 2. keep res array
        # 3. iterate intervals
        # 4. check if the current interval overlaps with the last interval
        # 5. if yes, update the ending value of the last added interval using max()
        # 6. if no, add this current interval to the res

        intervals.sort()
        res = [intervals[0]]
        for curr_start, curr_end in intervals[1:]:
            prev_start, prev_end = res[-1]
            if curr_start <= prev_end:
                res[-1][1] = max(prev_end, curr_end)
            else:
                res.append([curr_start, curr_end])
        
        return res
        
