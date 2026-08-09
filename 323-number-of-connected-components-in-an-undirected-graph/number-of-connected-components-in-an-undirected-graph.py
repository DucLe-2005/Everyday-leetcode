class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # construct an adjacency list
        # iterate each node in adjacency list
        # if the node isn't visited, res += 1, bfs from that node, mark all connected nodes visited
        # time: O(V + E)
        # space: O(V + E)

        adjacency = defaultdict(list)
        for a, b in edges:
            adjacency[a].append(b)
            adjacency[b].append(a)
        
        res = 0
        visited = set()
        for node in adjacency:
            if node in visited:
                continue
            res += 1
            
            q = deque([node])
            while q:
                node = q.popleft()
                visited.add(node)

                for nei in adjacency[node]:
                    if nei not in visited:
                        q.append(nei)
            
        return res + n - len(visited)
            
