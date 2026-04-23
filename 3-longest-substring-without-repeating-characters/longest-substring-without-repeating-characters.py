class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        res = 0
        c_map = {}
        l = 0
        r = 0

        while r < len(s):
            while s[r] in c_map:
                del c_map[s[l]]
                l += 1
            c_map[s[r]] = r
            res = max(res, r - l + 1)
            r += 1
        
        return res