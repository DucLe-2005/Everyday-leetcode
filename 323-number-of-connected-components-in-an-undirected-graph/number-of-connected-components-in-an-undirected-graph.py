class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # time: O(V + Ea(V)), a(V) = inverse Ackermann function
        # space: O(V)
        parent = list(range(n))
        size = [1] * n

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            
            return parent[x]
        
        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return False
            
            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a
            
            parent[root_b] = root_a
            size[root_a] += size[root_b]

            return True
        
        components = n

        for a, b in edges:
            if union(a, b):
                components -= 1
        
        return components
