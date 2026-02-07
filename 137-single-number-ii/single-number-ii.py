class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        countMap = defaultdict(int)

        for num in nums:
            countMap[num] += 1

        print(countMap)
        for num in countMap:
            if countMap[num] == 1:
                return num