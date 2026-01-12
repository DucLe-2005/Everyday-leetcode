class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Bottom-up DP
        size = len(s)
        dp = [False] * (size + 1)  # s[i:] can form words from wordDict
        dp[size] = True
        

        for i in range(size, -1, -1):
            for w in wordDict:
                if i + len(w) <= size and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0] 