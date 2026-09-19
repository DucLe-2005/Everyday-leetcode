class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        parent = [i for i in range(len(edges) + 1)]
        size = [1] * (len(edges) + 1)

        def find(x: int) -> int:
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a: int, b: int) -> bool:
            parent_a = find(a)
            parent_b = find(b)

            if parent_a == parent_b:
                return False
            
            if size[parent_a] < size[parent_b]:
                parent_a, parent_b = parent_b, parent_a
            
            parent[parent_b] = parent_a
            size[parent_a] += size[parent_b]

            return True
        
        for a, b in edges:
            if not union(a, b):
                return [a, b]

            
