class Solution:
    def countAndSay(self, n: int) -> str:
        # base case: n = 1` -> return "1"
        # call prev = self.countAndSay(n - 1)
        # transform the string to RLE
        # time: O(n * m). m is the longest length of an RLE
        # space: O(1)

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
