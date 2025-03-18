class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        substrings = {}
        left = 0
        right = k
        ans = 0

        while right <= len(s):
            substring = s[left:right]
            if substring in substrings:
                substrings[substring] += 1
            else:
                substrings[substring] = 1
            left += 1
            right += 1

        for substring in substrings:
            if (len(substring) == len(set(substring))):
                ans += substrings[substring]
        
        return ans
