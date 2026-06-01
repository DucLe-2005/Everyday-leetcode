class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even_count = defaultdict(int)
        for num in nums:
            if num % 2 == 0:
                even_count[num] += 1
        
        res = -1
        max_count = 0
        for num, count in even_count.items():
            if count > max_count:
                max_count = count
                res = num
            elif count == max_count and num < res:
                res = num
        
        return res