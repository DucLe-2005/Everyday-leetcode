class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # time: O(n)
        # space: O(n)
        nums_set = set(nums)
        memo = {}

        def dfs(x):
            if x in memo:
                return memo[x]
            
            nxt = x ** 2
            if nxt not in nums_set:
                memo[x] = 1
            else:
                memo[x] = 1 + dfs(nxt)
            
            return memo[x]
        
        res = -1

        for num in nums_set:
            length = dfs(num)
            if length >= 2:
                res = max(res, length)
        
        return res