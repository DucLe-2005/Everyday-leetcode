class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # time: 
        candidates.sort()
        res = []

        def dfs(i: int, combination: List[int], curr_sum: int) -> None:
            if curr_sum > target:
                return
            if curr_sum == target:
                res.append(combination.copy())
                return
            
            for i in range(i, len(candidates)):
                combination.append(candidates[i])
                dfs(i, combination, curr_sum + candidates[i])
                combination.pop()
        
        dfs(0, [], 0)
        return res