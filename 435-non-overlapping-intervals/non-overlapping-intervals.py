class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        ordered = sorted(intervals, key=lambda x: (x[1], x[0]))
        kept = 0
        last_end = float("-inf")

        for start, end in ordered:
            if start >= last_end:
                kept += 1
                last_end = end

        return len(intervals) - kept