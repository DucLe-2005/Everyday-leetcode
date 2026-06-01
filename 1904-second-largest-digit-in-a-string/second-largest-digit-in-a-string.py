class Solution:
    def secondHighest(self, s: str) -> int:
        # big1 -> big2
        big1 = big2 = -1
        for c in s:
            if c in "0123456789":
                c = int(c)
                if c == big1 or c == big2:
                    continue
                if c > big2:
                    big1 = big2
                    big2 = c
                elif c > big1:
                    big1 = c
        
        return big1