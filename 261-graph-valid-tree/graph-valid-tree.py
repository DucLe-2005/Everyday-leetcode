class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # create an adjacency list. key: node, values: list of neighbors
        # create a visit set
        # if node is already in visit set, then a cycle is detected and it is not a valid tree

        adj = {i: [] for i in range(n)}

        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        visited = set()


        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)

            for neighbor in adj[node]:
                if neighbor != prev and not dfs(neighbor, node):
                    return False
            
            return True
        
        return dfs(0, -1) and len(visited) == n