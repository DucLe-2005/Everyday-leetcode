class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return 0

        window, mapT = {}, {}
        for c in t:
            mapT[c] = 1 + mapT.get(c, 0)
        
        have, need = 0, len(mapT)
        l = 0
        res = [l, 1]
        resLen = float("inf")
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in mapT and window[c] == mapT[c]:
                have += 1
            
            while have == need:
                # update the result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                # pop from the left of window
                window[s[l]] -= 1
                if s[l] in mapT and window[s[l]] < mapT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""



                
