class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # time: O(E + V)
        # space: O(E + V)
        graph = defaultdict(list)
        needed_count = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            needed_count[course] += 1
        
        q = deque()
        for i in range(numCourses):
            if needed_count[i] == 0:
                q.append(i)  
        
        order = []
        while q:
            item = q.popleft()
            order.append(item)
            for course in graph[item]:
                needed_count[course] -= 1
                if needed_count[course] == 0:
                    q.append(course)
        
        return order if len(order) == numCourses else []
