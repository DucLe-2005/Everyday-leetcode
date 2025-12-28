class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        stack = []
        size = len(height)

        for i in range(size):
            while stack and height[i] > height[stack[-1]]:
                top = stack[-1]
                stack.pop()

                if not stack:
                    break

                distance = i - stack[-1] - 1
                bounded_height = min(height[i], height[stack[-1]]) -  height[top]
                res += bounded_height * distance
            stack.append(i)
        return res

