class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # time: O(N + R), N = len(numcourses), R = len(prerequisites)
        # space: O(N + R)
        graph = defaultdict(list)
        needed_count = [0] * numCourses
        for course, prereq in prerequisites:
            needed_count[course] += 1
            graph[prereq].append(course)
        
        q = deque([])
        for course in range(numCourses):
            if needed_count[course] == 0:
                q.append(course)

        count = 0
        while q:
            item = q.popleft()
            count += 1
            for course in graph[item]:
                needed_count[course] -= 1
                if needed_count[course] == 0:
                    q.append(course)
        
        return count == numCourses
