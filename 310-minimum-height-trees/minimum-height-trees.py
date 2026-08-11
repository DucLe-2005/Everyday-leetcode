class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # time: O(n)
        # space: O(n)

        if n == 1:
            return [0]

        graph = defaultdict(list)
        degree = [0] * n

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1
        
        q = deque([])
        for i in range(n):
            if degree[i] == 1:
                q.append(i)

        remaining = n
        while remaining > 2:
            leaf_count = len(q)
            remaining -= leaf_count

            for _ in range(len(q)):
                node = q.popleft()

                for nei in graph[node]:
                    degree[nei] -= 1

                    if degree[nei] == 1:
                        q.append(nei)
        
        return list(q)
