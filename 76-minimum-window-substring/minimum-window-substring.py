class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        sCount, tCount = {}, {}
        for c in t:
            tCount[c] = tCount.get(c, 0) + 1

        have = 0
        need = len(tCount)
        res = ""
        min_len = float("inf")
        l = 0 
        for r in range(len(s)):  # sliding windows to find the min substring that includes every char in t
            sCount[s[r]] = sCount.get(s[r], 0) + 1

            if s[r] in tCount and sCount[s[r]] == tCount[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < min_len:
                    res = s[l: r + 1]
                    min_len = r - l + 1


                sCount[s[l]] -= 1
                if s[l] in tCount and sCount[s[l]] < tCount[s[l]]:
                    have -= 1
                
                l += 1
            
        return res