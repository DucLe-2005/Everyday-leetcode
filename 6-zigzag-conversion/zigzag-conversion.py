class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows:
            return s
        
        res = [[] for _ in range(numRows)]
        step = 1
        idx = 0

        for i in range(len(s)):
            res[idx].append(s[i])

            if idx + step == numRows:
                step = -1
            elif idx + step < 0:
                step = 1
            
            idx += step
        
        return "".join(["".join(x) for x in res])
