class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        num_set = set()
        left = 0
        ans = 0

        for right in range(len(s)):
            while s[right] in num_set:
                num_set.remove(s[left])
                left += 1
            num_set.add(s[right])
            if right - left + 1 >= k:
                ans += 1
            
        return ans