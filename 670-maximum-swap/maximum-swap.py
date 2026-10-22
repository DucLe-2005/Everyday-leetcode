class Solution:
    def maximumSwap(self, num: int) -> int: 
        # for each number from left to right
        # swap that number with the larger number to the number on the right (if present)

        # if there are multple largest numbers to the right, swap with the rightmost number
        
        # 238909 -> 938909
        digits = list(str(num))
        last = {}

        for i, d in enumerate(digits):
            last[d] = i

        print(last)
        for i in range(len(digits)):
            for j in range(9, int(digits[i]), - 1):
                if str(j) in last and last[str(j)] > i:
                    digits[i], digits[last[str(j)]] = digits[last[str(j)]], digits[i]
                    return int("".join(digits))
        
        return num
