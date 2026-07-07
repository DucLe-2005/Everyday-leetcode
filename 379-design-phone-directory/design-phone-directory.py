class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.next_num = 0
        self.released = set()
        self.used = set()
        self.maxNumbers = maxNumbers

    def get(self) -> int:
        if self.released:
            num = self.released.pop()
        elif self.next_num < self.maxNumbers:
            num = self.next_num
            self.next_num += 1
        else:
            return -1
        
        self.used.add(num)
        return num

    def check(self, number: int) -> bool:
        return number in self.released or number >= self.next_num

    def release(self, number: int) -> None:
        if number not in self.used:
            return
        self.used.remove(number)
        self.released.add(number)

# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)