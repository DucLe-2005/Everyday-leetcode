class Solution:
    def numTrees(self, n: int) -> int:
        self.count = 0

        @lru_cache(maxsize=None)
        def dfs(lower, upper):
            if lower >= upper:
                return 1
            
            count = 0
            for i in range(lower, upper + 1):
                left_count = dfs(lower, i - 1)
                right_count = dfs(i + 1, upper)
                count += right_count * left_count
            
            return count
        
        return dfs(1, n)