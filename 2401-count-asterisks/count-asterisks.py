class Solution:
    def countAsterisks(self, s: str) -> int:
        res = 0
        is_between = False
        for c in s:
            if c == "|":
                is_between = not is_between
            else:
                if not is_between and c == "*":
                    res += 1
        
        return res