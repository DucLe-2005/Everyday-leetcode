class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        def helper(x_shift, y_shift):
            num = 0
            for r in range(n):
                for c in range(n):
                    if 0 <= c + x_shift < n and 0 <= r + y_shift < n and img1[r + y_shift][c + x_shift] == img2[r][c] and img2[r][c] == 1:
                        num += 1
            return num

        res = 0
        for x in range(-n + 1, n, 1):
            for y in range(-n + 1, n, 1):
                res = max(res, (helper(x, y)))

        return res
