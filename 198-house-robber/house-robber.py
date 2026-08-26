class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1 -> rob2 -> curr
        rob1 = rob2 = 0
        for num in nums:
            new_rob = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = new_rob
        
        return rob2