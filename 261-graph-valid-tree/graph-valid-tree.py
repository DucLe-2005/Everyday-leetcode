class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # a valid tree -> no circle, connected
        # time: O(V + E)
        # space: O(V + E)
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        q = deque([(0, -1)])
        
        visited = set()
        while q:
            node, parent = q.popleft()
            visited.add(node)

            for nei in graph[node]:
                print(f"node: {node}, nei: {nei}")
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                q.append((nei, node))
            
        return len(visited) == n