class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()

        @lru_cache(maxsize=None)
        def dfs(remain):
            if remain == 0:
                return 1
            if remain < 0:
                return 0
            
            combinations = 0
            for num in nums:
                if num > remain:
                    break
                combinations += dfs(remain - num)
            
            return combinations

        return dfs(target)