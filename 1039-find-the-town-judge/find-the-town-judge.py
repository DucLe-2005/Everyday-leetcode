class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # time: O(V + E)
        # space: O(V)
        if not trust:
            return n if n == 1 else -1

        indegree = defaultdict(int)
        outdegree = defaultdict(int)

        for a, b in trust:
            indegree[b] += 1
            outdegree[a] += 1
        
        for p in indegree:
            if indegree[p] == n - 1 and outdegree[p] == 0:
                return p
        
        return - 1