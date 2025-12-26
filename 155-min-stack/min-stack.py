class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []  # monotonic increasing stack

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        tmp = []
        while self.min_stack and self.min_stack[-1] < val:
            tmp.append(self.min_stack.pop())
        self.min_stack.append(val)
        
        while tmp:
            self.min_stack.append(tmp.pop())

    def pop(self) -> None:
        pop = self.stack.pop()

        
        if self.min_stack[-1] == pop:
            self.min_stack.pop()
        else:
            tmp = []
            while self.min_stack[-1] != pop:
                tmp.append(self.min_stack.pop())
            self.min_stack.pop()

            while tmp:
                self.min_stack.append(tmp.pop())
        
        return pop

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()