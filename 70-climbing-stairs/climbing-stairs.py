class Solution:
    def climbStairs(self, n: int) -> int:
        # DP
        # Reasoning: 
        # At stair i, to get to the top, there are n - i steps.
        # the number of ways that I can climb to the top is the sume of:
        # 1. the number of ways that I can climb to the top from stair n + 1
        # 2. the number of ways that I can climb to the top from stair n + 2
        # At the top (stair n), there is only 1 way for me to get to the top   
        # At stair n - 1, there is only 1 way for me to get to the top (by climb 1 step)
        # dp[i] = dp[i+1] + dp[i+2]
        # time: O(n), space: O(1)

        two_steps = 1
        one_step = 1
        for i in range(n - 2, -1, -1):
            curr = two_steps + one_step
            two_steps = one_step
            one_step = curr
        
        return one_step
        