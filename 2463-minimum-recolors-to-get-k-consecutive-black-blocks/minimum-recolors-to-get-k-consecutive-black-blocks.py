class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # iterate blocks with a window of length k
        # for each window, count number of white blocks
        # record the smallest number of whites blocks

        res = k
        whites = 0
        l = 0
        for r in range(len(blocks)):
            if blocks[r] == "W":
                whites += 1
            
            if r - l + 1 > k:
                if blocks[l] == "W":
                    whites -= 1
                l += 1
                
            if r - l + 1 == k:
                res = min(res, whites)
        
        return res