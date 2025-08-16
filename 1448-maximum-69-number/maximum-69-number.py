class Solution:
    def maximum69Number (self, num: int) -> int:
        a = list(str(num))
        for n in range(len(a)):
            if a[n] == "6":
                a[n] = "9"
                break
        
        return int("".join(a))
