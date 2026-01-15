class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]

        # dp[0][0] = 0 
        # dp[0][1] = 0
        # dp[0][2] = 0
        # dp[0][3] = 0

        # dp[1][1] =  1
        # dp[1][2] = 1
        # dp[1][3] = 1

        # dp[2][1] = 1
        # dp[2][2] = 1
        # dp[2][3] = 1

        # dp[3][1] = 1
        # dp[3][2] = dp[2][1] + 1 = 2
        # dp[3][3] = dp[3][2] = 2

        # dp[4][1] = 1
        # dp[4][2] = 2
        # dp[4][3] = 2
        
        # dp[5][1] = 1
        # dp[5][2] = 2
        # dp[5][3] = dp[4][2] + 1 = 2 + 1 = 

        # dp[1][0] = 


        # dp[1][0] = dp[0][0] = 1
        # dp[2][0] = dp[1][0] = 1
        # dp[3][0] = 1
        # dp[4][0] = 1


        # dp[0][1] = dp 




        # dp[i][j] = length of longest common subsequence of strings text1[0:i] and text2[0:j]

        # the lenght of longest common subsquence of strings text1[0:i] and text2[0:j]
        # = the length of the longest common subsequence of strings text1[0:i-1] and text2[0:j-1] + 1 (if text1[i] == text2[i])
        # = the length of the longest common subsequence of strings text1[0:i] and text2[0:j-1] 





