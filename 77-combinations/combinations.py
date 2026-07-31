class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # time: O(2^n + k * C(n, k))
        # space: O(n)
        res = []

        def dfs(i: int, combination: List[int]) -> None:
            nonlocal res
            if len(combination) == k:
                res.append(combination[:])
                return
            if i > n:
                return
            
            dfs(i + 1, combination)
            combination.append(i)
            dfs(i + 1, combination)
            combination.pop()
        
        dfs(1, [])
        return res