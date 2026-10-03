class Solution:
    def waysToSplit(self, nums: list[int]) -> int:
        prefix = [nums[0]]
        for num in nums[1:]:
            prefix.append(prefix[-1] + num)
        
        n = len(nums)
        res = 0
        for i in range(n - 2):
            left = prefix[i]
            if left * 2 > prefix[-1] - left:
                break
            
            # lower boundary: left <= middle 
            l = i + 1
            r = n - 2
            while l <= r:
                m = (l + r) // 2
                middle = prefix[m] - left

                if middle < left:
                    l = m + 1
                else:
                    r = m - 1
            
            lower = l

            # upper boundary: middle <= right
            l = i + 1
            r = n - 2
            while l <= r:
                m = (l + r) // 2
                middle = prefix[m] - left
                right = prefix[-1] - prefix[m]

                if middle > right:
                    r = m - 1
                else:
                    l = m + 1
            
            higher = r
            # print(f"i: {i}, lower: {lower}, higher: {higher}")
            res += higher - lower + 1
        
        return res % (10**9 + 7)