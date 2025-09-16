class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # use hash table to count nums occurences
        # k = 0 means finding duplicates
        # k > 0 means finding pairs
        # for k = 0, add 1 if val >= 2
        # for k > 0, add 1 if k - num is in the hash table, make sure not double counting by checking num <  k - num:

        d = Counter(nums)
        res = 0
        if k == 0:
            for val in d.values():
                if val >= 2:
                    res += 1
        else:
            for n in d:
                if n + k in d:
                    res += 1

        return res