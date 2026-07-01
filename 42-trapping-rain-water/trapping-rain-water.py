class Solution:
    def trap(self, height: List[int]) -> int:
        # time: O(n)
        # space: O(1)

        n = len(height)
        res = 0
        left_max, right_max = height[0], height[n-1]
        l, r = 0, n-1
        i = 0 if left_max < right_max else n - 1
        while l < r:
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])
            res += max(min(left_max, right_max) - height[i], 0)

            if left_max < right_max:
                l += 1
                i = l
            else:
                r -= 1
                i = r
        
        return res

                