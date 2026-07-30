class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # time: O(n ^ (target / m)), n = len(candidates), m = min(candidates)
        # space: O(target / m)
        candidates.sort()
        res = []

        def dfs(start: int, combination: List[int], remaining: int) -> None:
            if remaining == 0:
                res.append(combination[:])
                return
            
            for i in range(start, len(candidates)):
                if remaining < candidates[i]:
                    break

                combination.append(candidates[i])
                dfs(i, combination, remaining - candidates[i])
                combination.pop()
        
        dfs(0, [], target)
        return res