class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        decode1, decode2 = 1, 0
        # [i, decode1, decode2]
        for i in range(n - 1, -1, -1):
            newDecode = 0
            if s[i] != "0":
                newDecode = decode1
            if (i + 1 < n and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456")):
                newDecode += decode2
            
            decode2 = decode1
            decode1 = newDecode
        
        return decode1
            