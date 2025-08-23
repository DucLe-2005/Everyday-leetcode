class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # time: O(nlog(n))
        # space: O(n)
        intervals.sort(key = lambda x : x[0])
        res = [intervals[0]]
        for start, end in intervals:
            prev = res[-1]
            if start <= prev[1]:
                prev[1] = max(end, prev[1])
            else:
                res.append([start, end])
        
        return res