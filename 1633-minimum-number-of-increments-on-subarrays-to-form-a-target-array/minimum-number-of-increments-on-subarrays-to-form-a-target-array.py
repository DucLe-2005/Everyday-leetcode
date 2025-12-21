class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # [3, 1, 5 ,4 ,2]
        # [2, 0, 4, 3, 2]
        # [1, 0, 4, 3, 2]
        # [0, 0, 4, 3, 2]
        # [0, 0, 3, 2, 1]
        # [0, 0, 2, 1, 0]
        # [0, 0 ,1, 0 ,0]
        # [0 ,0 ,0 ,0 ,0]

        # all_zeros = false  
        # res = 0 (count of number of operations)
        # iterate until find a non-zero number
        # decrement all adjacent non-zero numbers until reaches the end or another zero, res + 1
        # if i iterate the whole target array and all zero present, all_zeroes = True
        # time: O(n * m), m = # of ops, n = length of target
        # space: O(1)


        # initalize 'prev' to keep track the # of operations needed for the previous number
        # iterate each number in target:
        # if the number of operation needed for the current number > prev, increase res by the difference
        # if the number of operation needed for the currentn number < prev   
        # update prev for both conditions

        res = 0
        prev = 0
        for num in target:
            if num > prev:
                res += num - prev
            prev = num
        
        return res



