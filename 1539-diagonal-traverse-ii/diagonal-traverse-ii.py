class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # traverse each column form left right from top row to bottom row
        # add the number to the hash table with indexes sum being the key: (row + colum ): [a, b, c]
        # after adding all numbers to the has table, append all items in values' arrays to the result

       
        d = defaultdict(list)
        for r in range(len(nums)):
            for c in range(len(nums[r])):
                d[r + c].append(nums[r][c])
        
        res = []
        for vals in d.values():
            for n in vals[::-1]:
                res.append(n)
        
        return res
