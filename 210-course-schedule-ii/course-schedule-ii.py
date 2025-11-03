class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for child, parent in prerequisites:
            graph[parent].append(child)
            indegree[child] += 1
        
        zeroDegree = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                zeroDegree.append(i)
            
        res = []
        while zeroDegree:
            course = zeroDegree.popleft()
            res.append(course)
            
            for child in graph[course]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    zeroDegree.append(child)
        
        for i in indegree:
            if i != 0:
                return []
        return res
        


       