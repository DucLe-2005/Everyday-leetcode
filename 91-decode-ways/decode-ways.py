class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1] * (len(s) + 2)
        dp[-1] = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
                continue
            dp[i] = dp[i+1]
            if (s[i] == "1" or (s[i] == "2" and i + 1 < len(s) and s[i+1] in "0123456")):
                dp[i] += dp[i+2]
        
        return dp[0]

        # time complexity: O(n)   
        # space complexity: O(n)
