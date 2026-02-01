class Solution:
    def numDecodings(self, s: str) -> int:
        # [i, decode1, decode2]
        decode1, decode2 = 1, 0
        for i in range(len(s) - 1, -1, -1):
            new_decode = decode1
            if s[i] == "0":
                new_decode = 0
            elif (s[i] == "1" or (s[i] == "2" and i + 1 < len(s) and s[i+1] in "0123456")):
                new_decode += decode2

            decode2 = decode1
            decode1 = new_decode
        
        return decode1

        # time complexity: O(n)   
        # space complexity: O(1)
