class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # time: O(nlogn)
        # space: O(n)
        expected = sorted(heights)

        res = 0
        for i in range(len(expected)):
            if expected[i] != heights[i]:
                res += 1
        
        return res