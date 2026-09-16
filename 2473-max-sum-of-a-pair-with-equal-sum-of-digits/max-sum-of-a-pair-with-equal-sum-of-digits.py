class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        num_map = defaultdict(list)

        for num in nums:
            x = num
            digit_sum = 0
            while x:
                digit_sum += x % 10
                x //= 10
            
            num_map[digit_sum].append(num)
        
        res = -1
        for arr in num_map.values():
            if len(arr) > 1:
                res = max(res, self.largestPairSum(arr))
        
        return res
    
    def largestPairSum(self, nums):
        first = 0
        second = 0

        for num in nums:
            if num > first:
                second = first
                first = num
            elif num > second:
                second = num
        
        return first + second
            