class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # keep track of characters in window
        # move l pointer if distinct chars > 2
        # move r pointer otherwise
        # update the length as r moves

        chars = {}
        s = list(s)
        l = 0
        res = 0
        for r in range(len(s)):
            chars[s[r]] = chars.get(s[r], 0) + 1
            while len(chars) > 2:
                chars[s[l]] -= 1
                if chars[s[l]] == 0:
                    del chars[s[l]]
                l += 1
            res = max(res, r - l + 1)

        return res