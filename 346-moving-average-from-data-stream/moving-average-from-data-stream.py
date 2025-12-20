class MovingAverage:

    def __init__(self, size: int):
        self.window = deque()
        self.current_size = 0
        self.size = size
        self.cur_sum = 0

    def next(self, val: int) -> float:
        if self.current_size < self.size:
            self.current_size += 1
            self.window.append(val)
            self.cur_sum += val
        else:
            self.cur_sum -= self.window.popleft()
            self.window.append(val)
            self.cur_sum += val
        
        return self.cur_sum / self.current_size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)