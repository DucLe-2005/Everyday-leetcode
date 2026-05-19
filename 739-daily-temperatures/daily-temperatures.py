class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # initialize answers = [0] * len(temperatures)
        # declare a stack that is monotonically decreasing
        # traverse temperatures
        # if temp is lower than top of the stack, add to stack
        # if temp is higher than top of the stack, pop the stack, set answers[i] = temperatures[i] - stack.pop()
        # time: O(n)
        # space: O(n)

        stack = []
        answer = [0 for _ in range(len(temperatures))]

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                prev_i, prev_temp = stack.pop()
                answer[prev_i] = i - prev_i
            stack.append((i, temp))
        return answer