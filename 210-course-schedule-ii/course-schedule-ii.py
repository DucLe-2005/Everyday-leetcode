class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prevMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prevMap[crs].append(pre)

        visit = set()  # all courses along the current dfs course path
        added = set()  # courses added to the result
        res = []
        def dfs(crs):
            if crs in visit:
                return False
            if prevMap[crs] == []:
                if crs not in added:
                    res.append(crs)
                    added.add(crs)
                return True
            
            visit.add(crs)
            for pre in prevMap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            prevMap[crs] = []

            if crs not in added:
                res.append(crs)
                added.add(crs)

            return True
            
        for crs in prevMap:
            if not dfs(crs):
                return []
        
        return res
