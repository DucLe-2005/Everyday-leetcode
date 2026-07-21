class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # time: O(n * m * L), n = len(s), m = len(dictionary), L = average word length
        # space: O(n)

        n = len(s)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            # Default s[i] is an extra character
            dp[i] = dp[i+1] + 1

            for word in dictionary:
                if s.startswith(word, i):
                    dp[i] = min(dp[i], dp[i+len(word)])

        return dp[0]