class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_times = [i[0] for i in intervals]
        end_times = [i[1] for i in intervals]
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
            else:
                e += 1
                rooms -= 1
            
            res = max(res, rooms)
        
        return res