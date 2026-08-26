class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # time: O(n + u), n = len(nums), u = # of unique nums
        # space: O(u)
        num_count = defaultdict(int)
        for num in nums:
            num_count[num] += 1
        
        # earn1 -> earn2 -> curr
        prev_num = -1
        earn1 = earn2 = 0
        for num in sorted(num_count):
            if num - prev_num > 1:
                new_earn = num * num_count[num] + earn2
            else:
                new_earn = max(num * num_count[num] + earn1, earn2)
            
            prev_num = num
            earn1 = earn2
            earn2 = new_earn
        
        return earn2
        
        return earn2