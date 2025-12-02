class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list) 
        # key: prerequisite course,  
        # values: list of courses that need this prereq
        indegree = [0] * numCourses  # number of prerequisites for each course

        # build the graph and indegree array
        for child, parent in prerequisites:
            graph[parent].append(child)
            indegree[child] += 1
        
        # Add course with no prerequisite to queue
        zero_queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                zero_queue.append(course)
        
        # Use BFS to determine the course order
        course_order = []
        while zero_queue:
            course = zero_queue.popleft()
            course_order.append(course)

            # Decrease the indegree of the course's children by 1
            for child in graph[course]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    zero_queue.append(child)
        
        # There is a cycle, so it is impossible to finish all courses
        if numCourses != len(course_order):
            return []
        return course_order


        # time: O(V + E)
        # space: O(V + E)