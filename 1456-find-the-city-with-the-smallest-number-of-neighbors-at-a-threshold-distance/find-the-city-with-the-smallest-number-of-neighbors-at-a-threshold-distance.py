class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # build an adjacency list
        # use Floyd Marshall algorithm to find the shortest distances from any cities
        # time: O(V^3)
        # space: O(V^2)
        matrix = [[inf for _ in range(n)] for _ in range(n)]
        for a, b, d in edges:
            matrix[a][b] = d
            matrix[b][a] = d

        for i in range(n):
            matrix[i][i] = 0
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

        print(f"matrix after: {matrix}")
        
        res = -1
        min_count = float("inf")
        for i, row in enumerate(matrix):
            reachable = sum(1 for dist in row if dist <= distanceThreshold)

            if reachable <= min_count:
                res = i
                min_count = reachable

        return res








