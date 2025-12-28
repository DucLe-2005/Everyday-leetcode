class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            print("curr:", temp)
            while stack and stack[-1][0] < temp:
                print("prev:", stack[-1][0])
                prev_temp, prev_idx = stack.pop()
                answer[prev_idx] = i - prev_idx

            stack.append((temp, i)) 
        
        return answer
