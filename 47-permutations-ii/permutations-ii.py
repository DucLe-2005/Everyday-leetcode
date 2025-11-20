class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []

        def backtrack(comb, counter):
            if len(comb) == len(nums):
                results.append(comb.copy())
            
            for num in counter:
                if counter[num] > 0:
                    counter[num] -= 1
                    comb.append(num)

                    backtrack(comb, counter)

                    comb.pop()
                    counter[num] += 1
        
        backtrack([], Counter(nums))
        return results