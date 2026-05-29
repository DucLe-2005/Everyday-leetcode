class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        has_duplicates = set()

        for num, c in count.items():
            if c > 1:
                has_duplicates.add(num)
        
        def update_if_unique(nums):
            for num in nums:
                count[num] -= 1
                if count[num] <= 1 and num in has_duplicates:
                    has_duplicates.remove(num)

        idx = 0
        res = 0
        while idx + 2 < len(nums):
            if len(has_duplicates) == 0:
                return res
            
            update_if_unique([nums[idx], nums[idx+1], nums[idx+2]])
            res += 1
            idx += 3
        
        if len(has_duplicates) > 0:
            print("res += 1")
            print(count)
            print(has_duplicates)
            res += 1
        
        return res



         