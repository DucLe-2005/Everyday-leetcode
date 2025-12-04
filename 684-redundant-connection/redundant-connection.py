class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # iterate each edge
        # union the two nodes
        # in the union function, if the two nodes have the same root, the that edge is redundant
        n = len(edges)
        parents = [i for i in range(n + 1)]
        sizes = [1 for _ in range(n + 1)]

        redundant_edge = []

        def find(A):
            root = A
            while root != parents[root]:
                root = parents[root]
            
            old_root = A
            while A != root:
                old_root = parents[A]
                parents[A] = root
                A = old_root
            
            return root
        
        def union(A, B):
            root_A = find(A)  
            root_B = find(B)  

            if root_A == root_B:
                return False
            
            if sizes[root_A] < sizes[root_B]:
                parents[root_A] = root_B
                sizes[root_A] += sizes[root_B]
                sizes[root_B] = sizes[root_A]
            else:
                parents[root_B] = root_A
                sizes[root_A] += sizes[root_B]
                sizes[root_B] = sizes[root_A]
            
            return True
        
        for A, B in edges:
            if not union(A, B):
                redundant_edge = [A, B]
        
        return redundant_edge