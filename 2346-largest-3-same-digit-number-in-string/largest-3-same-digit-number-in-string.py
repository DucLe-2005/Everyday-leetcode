class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        max_val = -float("inf")
        l = 0
        num_count = {}
        for r in range(len(num)):
            num_count[num[r]] = num_count.get(num[r], 0) + 1

            if r - l + 1 > 3:
                num_count[num[l]] -= 1
                l += 1
            
            if num_count[num[r]] == 3:
                if max_val < int(num[r] * 3):
                    res = num[r] * 3
                    max_val = int(num[r] * 3)

        return res