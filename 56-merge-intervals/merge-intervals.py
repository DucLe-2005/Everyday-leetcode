class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. sort the intervals
        # 2. keep res array
        # 3. iterate intervals
        # 4. check if the current interval overlaps with the last interval
        # that we added toe res
        # 5. if yes, update the ending value of the last added interval using max()
        # 6. if no, add this current interval to the res

        intervals.sort()
        res = [intervals[0]]
        for s1, e1 in intervals[1:]:
            s2, e2 = res[-1]
            if s1 <= e2:
                res[-1][1] = max(e1, e2)
            else:
                res.append([s1, e1])
        
        return res
        
