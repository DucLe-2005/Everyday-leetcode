class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # can't travel in circle -> total cost > total gas
        # if total gas > total cost, find the index where gas > cost as starting point
        # time: O(n)
        # space: O(1)
        if sum(cost) > sum(gas):
            return -1
        
        start_idx = 0
        gas_left = 0
        for i in range(len(gas)):
            gas_left += gas[i] - cost[i]
            if gas_left < 0:
                start_idx = i + 1
                gas_left = 0
            
        
        return start_idx
            