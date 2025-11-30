class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create an adjcency list
        # key = course, values: array of prerequisites
        # run dfs on each prereq
        # if a course reappears along the path, return False because no circle is allowed
        # if a course has no prereq, then return True
        # time: O(n)
        # space: O(n)
        if numCourses == 1:
            return True

        # key: course, values: prereqs
        adj = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj[course].append(prereq)
        
        visit = set()
        print(adj)

        def dfs(course):
            if course in visit:
                return False
            if adj[course] == []: # we have traverse this path
                return True

            visit.add(course)
            for pre in adj[course]:
                if not dfs(pre):
                    return False

            visit.remove(course)
            adj[course] = []  # the path is fully visited
            
            return True
        
        for course in adj:
            if not dfs(course):
                return False

        return True