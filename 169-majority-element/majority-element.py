class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for n, c in count.items():
            if c > len(nums) / 2:
                return n