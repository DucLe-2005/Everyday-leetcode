class Solution:
    def rob(self, nums: List[int]) -> int:
        # the total amount of money I have when at house i is:
        # max amount of money I had when at 2 houses back plus this house i
        # max amount of money I had when at the previous house
        # time: O(n), space: O(1)
        if len(nums) == 1:
            return nums[0]

        amount_1 = 0
        amount_2 = 0
        
        for money in nums:
            curr = max(amount_1, amount_2 + money)
            amount_2 = amount_1
            amount_1 = curr

        return curr
