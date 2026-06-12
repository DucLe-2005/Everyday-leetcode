class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        res = []
        for num in nums:
            if res and res[-1] == num:
                continue
            c = min(count[num], k)
            for _ in range(c):
                res.append(num)
        
        return res