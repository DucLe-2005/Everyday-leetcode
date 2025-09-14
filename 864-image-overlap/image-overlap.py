class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        # Record the coordinates of 1's in img1
        A = []
        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    A.append((r, c))
        
        # Record the coordinates of 1's in img2
        B = []
        for r in range(n):
            for c in range(n):
                if img2[r][c] == 1:
                    B.append((r, c))
        
        # If either image has no 1's, there is no overlap
        if not A or not B:
            return 0
        
        # Use a hash table to count occurences of translation vectors
        d = collections.defaultdict(int)
        for ax, ay in A:
            for bx, by in B:
                x_diff = bx - ax
                y_diff = by - ay
                d[(x_diff, y_diff)] += 1
        
        # The largest value in the hash table is the maximum overlap
        return max(d.values())
