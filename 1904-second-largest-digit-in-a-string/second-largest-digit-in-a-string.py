class Solution:
    def secondHighest(self, s: str) -> int:
        # big1 -> big2
        big1 = big2 = -1
        for c in s:
            if c.isdigit():
                c = int(c)
                if c > big2:
                    big1, big2 = big2, c
                elif big1 < c < big2:
                    big1 = c
        
        return big1