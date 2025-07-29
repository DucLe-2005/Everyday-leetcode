class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        def isAlphaNumberic(c: str):
            return (ord('A') <= ord(c) <= ord('Z') or
                    ord('a') <= ord(c) <= ord('z') or 
                    ord('0') <= ord(c) <= ord('9'))

        while l <= r:
            if not isAlphaNumberic(s[l]):
                l += 1
            elif not isAlphaNumberic(s[r]):
                r -= 1
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1

        return True