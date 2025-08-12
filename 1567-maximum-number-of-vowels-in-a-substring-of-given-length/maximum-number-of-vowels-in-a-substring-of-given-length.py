class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # curSum = current sum of the 
        # if curSum > maxSum => update maxSum
        # move left pointer and right pointer
        vowels = ['a', 'e', 'i', 'o', 'u']
        curSum = 0
        maxSum = 0
        for i in s[0:k]:
            if i in vowels:
                curSum += 1
        
        maxSum = curSum
        for i in range(k, len(s)):
            if s[i] in vowels:
                curSum += 1
            
            if s[i-k] in vowels:
                curSum -= 1
            
            maxSum = max(maxSum, curSum)
        
        return maxSum
    


