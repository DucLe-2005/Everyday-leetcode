class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # use backtrack
        # once reach length = k and sum = n, append to result, stop the recursion stack
        # the recursion call will not use the current or previous number again

        res = []

        def dfs(total, path, start):
            if total == n and len(path) == k:
                res.append(path[:])
                return
            if total > n and len(path) == k:
                return
            
            for i in range(start, 10):
                path.append(i)
                dfs(total+i, path, i + 1)
                path.pop()
        
        dfs(0, [], 1)

        return res