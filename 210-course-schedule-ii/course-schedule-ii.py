class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
       # Build graph: pre -> course
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[pre].append(course)
        
        color = [0] * numCourses  # 0=unvisited, 1=visiting, 2=done
        order = []               # post order

        def dfs(u):
            if color[u] == 1:    # cycle
                return False
            if color[u] == 2:    # already processed
                return True
            

            color[u] = 1
            for v in graph[u]:
                if not dfs(v):
                    return False

            color[u] = 2
            order.append(u)
            return True
        
        for u in range(numCourses):
            if color[u] == 0:
                if not dfs(u):
                    return []

        return order[::-1]

       