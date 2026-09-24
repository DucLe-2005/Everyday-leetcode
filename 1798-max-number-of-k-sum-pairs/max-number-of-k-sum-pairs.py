class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        num_count = {}
        res = 0
        for num in nums:
            diff = k - num
            if diff in num_count:
                res += 1
                num_count[diff] -= 1

                if num_count[diff] == 0:
                    del num_count[diff]
            else:
                num_count[num] = num_count.get(num, 0) + 1
        
        return res