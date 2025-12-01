class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # time: O(V + )
        parents = [i for i in range(n)]
        sizes = [1 for _ in range(n)]
        component_count = n

        # ------- union find functions -------- #
        def find(A: int) -> int:
            root = A
            while root != parents[root]:
                root = parents[root]
            
            # update the root for the vertices on the path
            old_root = parents[A]
            while A != root:
                old_root = parents[A]
                parents[A] = root
                A = old_root
            
            return root
            
        def union(A: int, B: int) -> int:
            root_A = find(A)
            root_B = find(B)

            # if A and B are already connected, then don't decrease count
            if root_A == root_B:
                return 0
            
            # ensure the root of the larger set remain the root
            if sizes[root_A] < sizes[root_B]:
                parents[root_A] = root_B
                sizes[root_B] += sizes[root_A]
                sizes[root_A] = sizes[root_B]
            else:
                parents[root_B] = root_A
                sizes[root_B] += sizes[root_A]
                sizes[root_A] = sizes[root_B]
        
            return 1
            
        # ----------- end of union find functions ---------- #

        for A, B in edges:
            component_count -= union(A, B)
        
        return component_count
