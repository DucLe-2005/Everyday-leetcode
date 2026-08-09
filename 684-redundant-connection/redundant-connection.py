class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # time: O(na(n))
        # space: O(n)
        
        parent = list(range(len(edges) + 1))
        size = [0] * (len(edges) + 1)

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

        redundant = []
        for a, b in edges:
            if not union(a, b):
                redundant = [a, b]
        
        return redundant