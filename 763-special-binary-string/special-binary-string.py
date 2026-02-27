class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if len(s) <= 2:
            return s
        
        parts = []
        count = 0
        l = 0
        for r in range(len(s)):
            if s[r] == "1":
                count += 1
            else:
                count -= 1
            
            if count == 0:
                parts.append("1" + self.makeLargestSpecial(s[l+1:r]) + "0")
                l = r + 1
        
        parts.sort(reverse=True)
        return "".join(parts)


        # time: O(n^2 log(n))   
        # space: O(n)