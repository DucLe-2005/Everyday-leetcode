class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()  
        ORs = set() # ORs values of subarrays that end at arr[i]
        for num in arr:
            ORs = {num | x for x in ORs}
            ORs.add(num)
            res |= ORs
        
        return len(res)