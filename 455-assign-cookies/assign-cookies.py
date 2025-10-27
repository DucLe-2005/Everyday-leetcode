class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        cookie_idx = 0

        for greed in g:
            while cookie_idx < len(s) and s[cookie_idx] < greed:
                cookie_idx += 1
            
            if cookie_idx == len(s):
                return res
            
            res += 1
            cookie_idx += 1
    
        return res

            