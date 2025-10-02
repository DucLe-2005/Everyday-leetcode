class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_times = []
        end_times = []
        for i in intervals:
            start_times.append(i[0])
            end_times.append(i[1])
            
        start_times.sort()
        end_times.sort()
        rooms = 0
        res = 0
        s, e  = 0, 0

        while s < len(intervals):
            print(s, e)
            if start_times[s] < end_times[e]:
                s += 1
                rooms += 1
                res = max(res, rooms)
            else:
                e += 1
                rooms -= 1
            
        return res