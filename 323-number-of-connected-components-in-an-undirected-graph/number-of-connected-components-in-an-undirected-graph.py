class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create an adjacency table
        # do a dfs on all neighborsd; add the node to visited node
        # if the node is already visited, then stop the dfs.
        # increase count by 1 if a node is not in visited.

        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()  # visited nodes
        def dfs(i):
            if i in visited:
                return
            
            visited.add(i)
            for nei in adj[i]:
                if nei not in visited:
                    dfs(nei)

        count = 0
        for n in adj:
            if n not in visited:
                dfs(n)
                count += 1

        return count




