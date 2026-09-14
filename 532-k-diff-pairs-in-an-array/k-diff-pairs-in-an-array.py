class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1

        res = 0
        print(num_count)

        for num in num_count:
            print(f"num: {num}")
            if k == 0:
                res += 1 if num_count[num] > 1 else 0
            elif num - k in num_count:
                res += 1
            
            print(res)
        
        return res