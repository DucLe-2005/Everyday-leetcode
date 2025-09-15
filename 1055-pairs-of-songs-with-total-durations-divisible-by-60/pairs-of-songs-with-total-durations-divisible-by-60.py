class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
    # use a hash table to store the remainder of each song after dividing it by 60 (use % operation)
    # if two remainders' sum equals 60, then their numbers' sum equals 60
    # if a (60 - A_remainder) is in the hash table, add the value to result

        res = 0
        d = defaultdict(int)
        for t in time:
            r = t % 60
            res += d[60 - r]
            if r == 0:
                r = 60
            d[r] += 1
        
        return res
