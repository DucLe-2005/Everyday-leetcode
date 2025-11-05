class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = defaultdict(list)
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        edge_cnt = {}
        leaves = deque()
        for node, neighbors in adj.items():
            if len(neighbors) == 1:
                leaves.append(node)
            edge_cnt[node] = len(neighbors)
        
        while True:
            if n <= 2:
                return list(leaves)
            
            for i in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for nei in adj[node]:
                    edge_cnt[nei] -= 1
                    if edge_cnt[nei] == 1:
                        leaves.append(nei)
            

        
