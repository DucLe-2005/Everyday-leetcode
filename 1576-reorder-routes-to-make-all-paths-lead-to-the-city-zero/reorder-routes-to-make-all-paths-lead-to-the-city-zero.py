class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # create an adjacency list with original and artificial edges
        # dfs starting from 0
        # if an edge from the parent to its child is original, decrement 1 to the ans
        # if an edge from the parent to its child is artificial, increment 1 to the ans
        # once we finish finish one route to the end, we backtrack to the previous node's neighbor and
        # take on that route
        # caveat: we want all edges point to the parent, which consequently points to 0

        adj = defaultdict(list)
        for src, des in connections:
            adj[src].append((des, 1))
            adj[des].append((src, 0))
        
        self.count = 0
        def dfs(node, parent):
            for neighbor, sign in adj[node]:
                if neighbor != parent:
                    self.count += sign 
                    dfs(neighbor, node)

        dfs(0, -1)
        return self.count