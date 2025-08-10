class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for time in timePoints:
            minutes.append(int(time[:2]) * 60 + int(time[3:]))
        
        minutes.sort()

        min_diff = float("inf")
        for i in range(len(minutes) - 1):
            diff = minutes[i+1] - minutes[i]
            min_diff = min(min_diff, diff)
        
        # account for the difference between the first and last elements
        min_diff = min(min_diff, 24*60 - minutes[-1] + minutes[0])
        return min_diff
        
