class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # convert nums to 1 = odd and 0 = even
        d = []
        for n in nums:
            if n % 2 != 0:
                d.append(1)
            else:
                d.append(0)
        
        res = 0
        prefixSum = {0 : 1}
        curSum = 0
        for i in d:
            curSum += i
            diff = curSum - k
            res += prefixSum.get(diff, 0)
            prefixSum[curSum] = prefixSum.get(curSum, 0) + 1
        
        return res
       
