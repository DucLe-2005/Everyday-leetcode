# Last updated: 5/18/2025, 4:59:42 PM
class Codec:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + "#" + s
        
        return res
        

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            res.append(s[j + 1 : j + length + 1 ])
            i = j + length + 1
        
        return res