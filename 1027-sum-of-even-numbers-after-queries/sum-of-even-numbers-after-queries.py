class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # time: O(n)
        # space: O(n)

        total = 0
        for num in nums:
            if num % 2 == 0:
                total += num
        
        answers = [0] * len(queries)
        for i in range(len(queries)):
            val, idx = queries[i]
            new_val = nums[idx] + val
            if nums[idx] % 2 == 0:
                if new_val % 2 == 0: # both even
                    total = total - nums[idx] + new_val
                else: # old even, new odd
                    total -= nums[idx]
            else:
                if new_val % 2 == 0: # old odd, new even
                    total += new_val
            
            answers[i] = total
            nums[idx] = new_val
            
        return answers
