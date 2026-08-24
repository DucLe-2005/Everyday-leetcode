class Solution:
    def fib(self, n: int) -> int:
        
        @lru_cache(maxsize=None)
        def dfs(n: int) -> int:
            if n == 0:
                return 0
            if n == 1:
                return 1
            
            return dfs(n-1) + dfs(n-2)

        return dfs(n)