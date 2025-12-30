class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # add each interval's start time and end time to start_times and end_times
        # sort start_times and end_times
        # iterate start times and end times
        # if start time < end time: need 1 more room, update rooms_required 
        # if end time < star time: need 1 less room

        start_times = sorted([i[0] for i in intervals])
        end_times = sorted([i[1] for i in intervals])

        rooms_req = 0
        rooms_curr = 0
        size = len(intervals)
        s, e = 0, 0

        while s < size:
            if start_times[s] < end_times[e]:
                rooms_curr += 1
                rooms_req = max(rooms_req, rooms_curr)
                s += 1
            else:
                rooms_curr -= 1
                e += 1
        
        return rooms_req
