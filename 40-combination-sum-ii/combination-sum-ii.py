class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur[:])
                return
            
            if total > target:
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:  # avoid duplication in the same recursion depth
                    continue

                if total + candidates[j] > target:
                    break

                cur.append(candidates[j])
                dfs(j + 1, cur, total + candidates[j])
                cur.pop()

        dfs(0, [], 0)
        return res