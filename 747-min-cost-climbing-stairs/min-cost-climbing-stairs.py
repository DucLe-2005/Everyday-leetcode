class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = cost[:]
        dp.append(0) 
        print(dp)
        for i in range(len(cost) - 2, -1, -1):
            print(i)
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        
        return min(dp[0], dp[1])