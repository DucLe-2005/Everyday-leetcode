class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False

        parents = [i for i in range(n)]
        sizes = [1 for _ in range(n)]
        
        # -------- helper functions ---------- #
        def find(A: int) -> int:
            # find the root
            root = A
            while root != parents[root]:
                root = parents[root]

            # update the root to all vertices on the path
            old_root = parents[A]
            while A != root:
                old_root = parents[A]
                parents[A] = root
                A = old_root
            
            return root

        def union(A: int, B: int) -> bool:
            root_A = find(A)
            root_B = find(B)

            # a cycle is detected because two nodes have the same root
            if root_A == root_B:
                return False
            
            # ensure that the root of the larger set remains the root
            if sizes[root_A] < sizes[root_B]:
                parents[root_A] = root_B
                sizes[root_A] += sizes[root_B]
                sizes[root_B] = sizes[root_A]
            else:
                parents[root_B] = root_A
                sizes[root_A] += sizes[root_B]
                sizes[root_B] = sizes[root_A]

            return True

        # ---------- end of helper functions ---------- #

        for A, B in edges:
            if not union(A, B):
                return False
        
        return True




            
