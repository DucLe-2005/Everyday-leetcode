class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []

        sCount, pCount = {}, {}
        for i in range(len(p)):
            sCount[s[i]] = sCount.get(s[i], 0) + 1
            pCount[p[i]] = pCount.get(p[i], 0) + 1
        
        res = []
        if sCount == pCount:
            res.append(0)
        
        l = 0
        for r in range(len(p), len(s)):
            sCount[s[l]] -= 1
            sCount[s[r]] = sCount.get(s[r], 0) + 1

            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            
            if sCount == pCount:
                res.append(l + 1)
            l += 1
    
        return res
            
