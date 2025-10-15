class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(total, path, start):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                path.append(candidates[i])
                dfs(total + candidates[i], path, i+1)
                path.pop()
        
            return path
        
        dfs(0, [], 0)

        return res