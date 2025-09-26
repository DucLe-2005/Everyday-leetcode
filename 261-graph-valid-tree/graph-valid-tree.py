class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # create an adjacency list out of the edges
        # do a dfs on the neighbors of each node

        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
    
        visit = set()  # all visisted nodes along the dfs path

        def dfs(node, prev):
            if node in visit:
                return False
            
            visit.add(node)

            for neighbor in adj[node]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, node):
                    return False
            
            return True
        
        return dfs(0, -1) and len(visit) == n

