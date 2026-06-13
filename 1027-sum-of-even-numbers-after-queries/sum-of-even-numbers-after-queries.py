class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # time: O(n)
        # space: O(n)

        even_sum = 0
        for num in nums:
            if num % 2 == 0:
                even_sum += num
        
        answers = []
        for val, idx in queries:
            if nums[idx] % 2 == 0:
                even_sum -= nums[idx] 
            nums[idx] += val
            if nums[idx] % 2 == 0:
                even_sum += nums[idx]
            answers.append(even_sum)
            
        return answers
