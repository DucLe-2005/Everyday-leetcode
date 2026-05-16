class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # time: O(n)
        # space: O(n)

        num_count = {}
        freq = [[] for _ in range(len(nums))]

        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        
        for num, count in num_count.items():
            freq[count - 1].append(num)
        
        res = []
        for i in range(len(freq) -1, -1, -1):
            for num in freq[i]:
                res.append(num)
                k -= 1
                if k == 0:
                    return res
        
        return res
        