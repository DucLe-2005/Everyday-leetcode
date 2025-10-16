class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []  # (number, index)
        res = [-1] * len(nums)

        def helper():
            for i, num in enumerate(nums):
                while stack and num > stack[-1][0]:
                    n, idx = stack.pop()
                    res[idx] = num
                stack.append((num, i))

        helper()
        helper()

        return res  