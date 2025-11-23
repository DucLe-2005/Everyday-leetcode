class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        prev = self.countAndSay(n - 1)
        new_s = []
        i = 0
        
        while i < len(prev):
            count = 1
            while i + 1 < len(prev) and prev[i] == prev[i + 1]:
                i += 1
                count += 1
            
            condensed = str(count) + str(prev[i])
            new_s.append(condensed)
            i += 1
        
        return "".join(new_s)
