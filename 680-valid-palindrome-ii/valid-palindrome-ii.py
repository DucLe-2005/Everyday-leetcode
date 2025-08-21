class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        l, r = 0, len(s) - 1
        while l < r:
            # found a mismatch -> try both deletions
            if s[r] != s[l]:
                return checkPalindrome(s, l+1, r) or checkPalindrome(s, l, r-1)
            
            l += 1
            r -= 1
        
        return True