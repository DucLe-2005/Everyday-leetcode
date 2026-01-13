class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Reasoning: sub[i] stores the minimum possible tail of an increasing subsequence of length i + 1. Appending increases the best-known length only when we can extend an existing subsequence. Replacing improves tails withouth changing the best-known length. Therefore, the length of sub at the end equals the LIS length.
        sub = [nums[0]]

        # find the index of the smallest element that is greater
        # than or equal to num
        def find_index(sub, num):
            l, r = 0, len(sub)
            while l < r:
                m = (l + r) // 2
                if sub[m] >= num:
                    r = m
                else:
                    l = m + 1

            return l   

        for num in nums[1:]:
            i = find_index(sub, num)

            if i == len(sub):
                sub.append(num)
            else:
                sub[i] = num
        
        return len(sub)
        