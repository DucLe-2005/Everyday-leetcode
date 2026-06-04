class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # time: O(n)
        # space: O(n)
        subordinates = defaultdict(list)
        for i in range(n):
            if manager[i] == -1:
                continue
            subordinates[manager[i]].append(i)
        res = 0
        q = deque([(headID, informTime[headID])]) # (employeeId, time)
        while q:
            id, time = q.popleft()
            print(f"employee: {id}, time: {time}")
            res = max(res, time)
            for sub in subordinates[id]:
                if informTime[sub]:
                    q.append((sub, informTime[sub] + time))
        
        return res