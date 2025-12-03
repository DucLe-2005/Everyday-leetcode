class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for child, parent in prerequisites:
            graph[parent].append(child)
            indegree[child] += 1
        
        zero_queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                zero_queue.append(course)
        
        course_taken = 0
        while zero_queue:
            course = zero_queue.popleft()
            course_taken += 1

            for child in graph[course]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    zero_queue.append(child)
        
        return course_taken == numCourses