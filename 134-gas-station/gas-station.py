class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        cur = 0
        start = 0
        n = len(gas)
        
        for i in range(n):
            cur += gas[i] - cost[i]
            if cur < 0:
                start = i + 1
                cur = 0

        return start % n