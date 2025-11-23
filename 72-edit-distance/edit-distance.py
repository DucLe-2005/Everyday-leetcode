class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        self.memo = [[None] * (n + 1) for _ in range(m + 1)]
        return self.minDistanceRecur(word1, word2, len(word1), len(word2))
    
    def minDistanceRecur(self, word1, word2, index1, index2):
        if index1 == 0:
            return index2
        if index2 == 0:
            return index1
        
        if self.memo[index1][index2]:
            return self.memo[index1][index2]
        
        minDistance = 0
        if word1[index1 - 1] == word2[index2 - 1]:
            minDistance = self.minDistanceRecur(word1, word2, index1 - 1, index2 - 1) # skip char
        else:
            replace = self.minDistanceRecur(word1, word2, index1 - 1, index2 - 1)
            delete = self.minDistanceRecur(word1, word2, index1 - 1, index2)
            insert = self.minDistanceRecur(word1, word2, index1, index2 - 1)
            minDistance = min(replace, delete, insert) + 1
        
        self.memo[index1][index2] = minDistance
        return minDistance
    
    # time: O(m * n), m = len(word1), n = len(word2)
    # space: O(m * n), m = len(word1), n = len(word2)