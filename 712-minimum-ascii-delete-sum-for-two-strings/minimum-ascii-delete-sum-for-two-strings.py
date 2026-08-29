class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # at s1Index and s2Index, we can either:
        # delete s1[s1Index]: s1Index + 1
        # delete s2[s2Index]: s2Index + 1
        # if s1[s2Index] == s2[s2Index]: s2Index + 1, s1Index + 1

        dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        
        for j in range(1, len(s2) + 1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j] + ord(s1[i-1]), # delete s2[j-1]
                        dp[i][j-1] + ord(s2[j-1])  # delete s1[i-1]
                    )
        
        return dp[-1][-1]
