class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sort the nums list
        # maintain a variable updated along with the length of the current sequence
        # if the next number is larger than the current number by more than 1, reset the variable
        if len(nums) == 0:
            return 0

        nums_sorted = sorted(nums)
        max_length = 1
        curr_length = 1

        for i in range(len(nums_sorted) - 1):
            if nums_sorted[i] + 1 < nums_sorted[i+1]:
                curr_length = 1
            elif nums_sorted[i] + 1 == nums_sorted[i+1]:
                curr_length += 1
            max_length = max(max_length, curr_length)
        
        return max_length
