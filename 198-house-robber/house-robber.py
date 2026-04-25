class Solution:
    def rob(self, nums: List[int]) -> int:
        # money1 -> money2 -> curr
        money1 = 0
        money2 = 0

        for num in nums:
            curr_money = max(num + money1, money2)
            money1 = money2
            money2 = curr_money
        
        return money2
