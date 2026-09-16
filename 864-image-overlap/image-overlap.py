class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        ones1 = []
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    ones1.append([i, j])
        
        ones2 = []
        for i in range(n):
            for j in range(n):
                if img2[i][j] == 1:
                    ones2.append([i, j])
        
        if not ones1 or not ones2:
            return 0

        shifts = defaultdict(int)
        for a, b in ones1:
            for c, d in ones2:
                shifts[(a - c, b - d)] += 1
        
        return max(shifts.values())
