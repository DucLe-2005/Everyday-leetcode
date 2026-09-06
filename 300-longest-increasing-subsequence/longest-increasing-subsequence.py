class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # DP
        # time: O(n^2)
        # space: O(n)
        # dp = [1] * (len(nums) + 1)
        # for i in range(1, len(nums) + 1):
        #     for j in range(i):
        #         if nums[i - 1] > nums[j - 1]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        
        # return dp[-1]

        # greedy
        # time: O(n^2)
        # space: O(n)
        sub = [nums[0]]

        for num in nums:
            if num > sub[-1]:
                sub.append(num)
            else:
                i = 0
                while num > sub[i]:
                    i += 1
                sub[i] = num
        
        return len(sub)
