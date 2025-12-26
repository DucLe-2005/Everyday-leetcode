class MyStack:

    def __init__(self):
        self.input = deque()
        self.output = deque()

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        while len(self.input) > 1:
            self.output.append(self.input.popleft())
        
        pop =  self.input.popleft()
        while self.output:
            self.input.append(self.output.popleft())
        
        return pop
        

    def top(self) -> int:
        while len(self.input) > 1:
            self.output.append(self.input.popleft())
        
        pop =  self.input.popleft()
        while self.output:
            self.input.append(self.output.popleft())
        self.input.append(pop)
        
        return pop
        

    def empty(self) -> bool:
        return not self.input


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()