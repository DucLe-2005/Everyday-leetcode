class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = [[None for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

        def dfs(word1Index, word2Index):
            if word1Index == 0:
                return word2Index
            if word2Index == 0:
                return word1Index
            if memo[word1Index][word2Index]:
                return memo[word1Index][word2Index]
            
            
            if word1[word1Index-1] == word2[word2Index-1]:
                distance = dfs(word1Index - 1, word2Index - 1)
            else:
                distance = 1 + min(
                    dfs(word1Index - 1, word2Index - 1),
                    dfs(word1Index, word2Index - 1),
                    dfs(word1Index - 1, word2Index)
                )
            
            memo[word1Index][word2Index] = distance

            return distance

        return dfs(len(word1), len(word2))

