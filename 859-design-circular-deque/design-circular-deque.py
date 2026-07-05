class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.front_idx = 0
        self.rear_idx = 0
        self.current_size = 0
        self.max_size = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front_idx = (self.front_idx - 1) % self.max_size
        self.queue[self.front_idx] = value
        self.current_size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.rear_idx] = value
        self.rear_idx = (self.rear_idx + 1) % self.max_size
        self.current_size += 1
        return True
        
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front_idx = (self.front_idx + 1) % self.max_size
        self.current_size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear_idx = (self.rear_idx - 1) % self.max_size
        self.current_size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front_idx]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.rear_idx - 1) % self.max_size]

    def isEmpty(self) -> bool:
        return self.current_size == 0

    def isFull(self) -> bool:
        return self.current_size == self.max_size
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()