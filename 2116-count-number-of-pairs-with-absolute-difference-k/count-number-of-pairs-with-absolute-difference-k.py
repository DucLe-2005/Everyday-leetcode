class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num , 0) + 1

        res = 0
        for num in num_count:
            if num - k in num_count:
                res += num_count[num - k] * num_count[num]
        
        return res