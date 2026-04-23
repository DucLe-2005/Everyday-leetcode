class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sorted_candidates = sorted(candidates)
        res = []

        def dfs(path, total, start):
            if total == target:
                res.append(path.copy())
            if total > target:
                return
            
            for i in range(start, len(sorted_candidates)):
                if i > start and sorted_candidates[i] == sorted_candidates[i-1]:
                    continue
                path.append(sorted_candidates[i])
                dfs(path, total+sorted_candidates[i], i+1)  
                path.pop()
        
        dfs([], 0, 0)
        return res