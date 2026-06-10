class Solution:
    def countHomogenous(self, s: str) -> int:
        # count all homogeneous substrings can be made in a homogenous substring
        # "aaaa", "bbbbb"
        # time: O(n)
        # space: O(n)
        MOD = 10**9 + 7
        res = 1
        s = list(s)
        curr = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr += 1
            else:
                curr = 1
            
            res = (res + curr) % MOD
        
        return res
