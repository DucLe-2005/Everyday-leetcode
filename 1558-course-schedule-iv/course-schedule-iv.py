class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # time: O(V^3 + Q), Q = len(queries)
        # space: O(V^2)
        isReachable = [[False] * numCourses for _ in range(numCourses)]
        for a, b in prerequisites:
            isReachable[a][b] = True
        
        for course in range(numCourses):
            destinations = isReachable[course]
            queue = deque([])
            for i in range(numCourses):
                if destinations[i]:
                    queue.append(i)

            while queue:
                node = queue.popleft()
                for i in range(numCourses):
                    if isReachable[node][i] and not destinations[i]:
                        destinations[i] = True
                        queue.append(i)

        res = []
        for u, v in queries:
            res.append(isReachable[u][v])
        
        return res

