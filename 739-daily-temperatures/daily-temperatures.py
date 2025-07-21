class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for currentIndex, currentTemp in enumerate(temperatures):
            while stack and currentTemp > stack[-1][1]:
                prevIndex, prevTemp = stack.pop()
                res[prevIndex] = currentIndex - prevIndex
            
            stack.append([currentIndex, currentTemp])
        
        return res