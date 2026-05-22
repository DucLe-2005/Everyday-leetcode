class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # if square root of num is in n, add num: its square root to dictionary
        # find the longest chain in the dictionary
        # time: O(n)
        # space: O(n)
        nums_set = set(nums)
        square_roots = {}
        for num in nums_set:
            if num ** 2 in nums_set:
                square_roots[num ** 2] = num

        res = -1
        visited = set()
        for num in square_roots:
            visited.add(num)
            length = 2
            curr = num
            while square_roots[curr] in square_roots:
                curr = square_roots[curr]
                length += 1
            res = max(res, length)
        
        return res
