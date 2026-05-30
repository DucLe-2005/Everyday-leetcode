class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        res = []
        unit = 1
        while n:
            mod = n % 10
            if mod != 0:
                res.append(mod * unit)
            n = n // 10
            unit *= 10
        res.reverse()
        return res

