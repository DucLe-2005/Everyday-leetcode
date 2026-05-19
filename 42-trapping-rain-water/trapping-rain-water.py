class Solution:
    def trap(self, height: List[int]) -> int:
        # time: O(n)
        # space: O(1)
        res = 0
        left_max = height[0]
        right_max = height[-1]
        l = 0
        r = len(height) - 1
        while l < r:
            if right_max > left_max:
                res +=  left_max - height[l]
                l += 1
                left_max = max(height[l], left_max)

            else:
                res += right_max - height[r]
                r -= 1
                right_max = max(right_max, height[r])

        return res

