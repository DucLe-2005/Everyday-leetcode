class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [x for x in triangle[-1]]
        for row in triangle[-2::-1]:
            for i in range(len(row)):
                dp[i] = min(dp[i], dp[i+1]) + row[i]
        
        return dp[0]
            