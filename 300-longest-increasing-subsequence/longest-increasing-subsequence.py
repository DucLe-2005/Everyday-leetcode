class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Reasoning: sub[i] stores the minimum possible tail of an increasing subsequence of length i + 1. Appending increases the best-known length only when we can extend an existing subsequence. Replacing improves tails withouth changing the best-known length. Therefore, the length of sub at the end equals the LIS length.
        sub = [nums[0]]
        for num in nums[1:]:
            if num > sub[-1]:
                sub.append(num)
            else:
                i = 0
                while sub[i] < num:
                    i += 1
                sub[i] = num
        
        return len(sub)
        