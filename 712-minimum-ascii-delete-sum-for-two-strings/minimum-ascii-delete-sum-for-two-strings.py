class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # at s1Index and s2Index, we can either:
        # delete s1[s1Index]: s1Index + 1
        # delete s2[s2Index]: s2Index + 1
        # if s1[s2Index] == s2[s2Index]: s2Index + 1, s1Index + 1

        memo = [[None for _ in range(len(s2))] for _ in range(len(s1))]

        def dfs(s1Index, s2Index):
            if s1Index == len(s1):
                return sum(ord(s2[i]) for i in range(s2Index, len(s2)))
            if s2Index == len(s2):
                return sum(ord(s1[i]) for i in range(s1Index, len(s1)))
            if memo[s1Index][s2Index]:
                return memo[s1Index][s2Index]

            if s1[s1Index] == s2[s2Index]:
                lowest_sum = dfs(s1Index + 1, s2Index + 1)
            else:
                lowest_sum = min(
                    dfs(s1Index + 1, s2Index) + ord(s1[s1Index]),
                    dfs(s1Index, s2Index + 1) + ord(s2[s2Index])
                )
            
            memo[s1Index][s2Index] = lowest_sum
            return lowest_sum
        
        return dfs(0, 0)