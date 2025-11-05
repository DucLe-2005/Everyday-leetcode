class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()

        @lru_cache(maxsize=None)
        def dfs(remain):
            if remain == 0:
                return 1
            
            result = 0
            for n in nums:
                if remain - n < 0:
                    break
                result += dfs(remain - n)
            
            return result
        
        return dfs(target)