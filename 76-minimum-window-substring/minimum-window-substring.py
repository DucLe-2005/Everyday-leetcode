class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        window = {}
        hashMapT = {}
        for i in t:
            hashMapT[i] = hashMapT.get(i, 0) + 1
        
        l = 0
        res = [-1, -1]
        have = 0
        need = len(hashMapT)
        minLength = float("inf")

        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1

            if char in hashMapT and window[char] == hashMapT[char]:
                have += 1

            while have == need:
                windowLength =  r - l + 1
                if windowLength < minLength:
                    res = [l, r]
                    minLength = windowLength
                
                leftChar = s[l]
                window[leftChar] -= 1
                if leftChar in hashMapT and window[leftChar] < hashMapT[leftChar]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l : r+1] if minLength != float("inf") else ""

         
