class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # time: O(n^2)
        # space: O(1)
        s = [x for x in range(1, n+1)]
        l = n
        i = 0
        k -= 1
        while l > 1:
            i += k
            i %= l
            del s[i]
            l -= 1
        return s[0]


