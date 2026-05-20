class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # keep a monotonically increasing stack
        stack = [-1]
        res = 0

        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                res = max(res, height * width)
            stack.append(i)
        
        while stack[-1] != -1:
            height = heights[stack.pop()]
            width = len(heights) - stack[-1] - 1
            res = max(res, height * width)
        
        return res
