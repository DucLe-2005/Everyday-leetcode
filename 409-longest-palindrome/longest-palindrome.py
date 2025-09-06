class Solution:
    def longestPalindrome(self, s: str) -> int:
        middle = 0
        count = Counter(s)
        res = 0
        
        for c in count.values():
            if c % 2 == 0:
                res += c
            else:
                res += c - 1
                middle = 1
        
        return res + middle
