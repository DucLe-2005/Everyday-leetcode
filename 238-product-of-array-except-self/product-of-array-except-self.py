class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        output = []

        # first iteration to calculate the prefix product of nums[i]
        output.append(prefix)
        for num in nums[:-1]:
            prefix *= num
            output.append(prefix)
        
        # second iteration to calculate the postfix product of nums[i]
        output[-1] *= postfix
        i = len(output) - 2
        for num in nums[len(nums)-1:0:-1]:
            postfix *= num
            output[i] *= postfix
            i -= 1
        
        return output
            
        return output