class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.val_index = {}

    def insert(self, val: int) -> bool:
        if val in self.val_index:
            return False
        
        self.nums.append(val)
        self.val_index[val] = len(self.nums) - 1

    def remove(self, val: int) -> bool:
        if val in self.val_index:
            i = self.val_index[val]
            new_num = self.nums[-1]
            self.nums[i] = new_num  
            self.val_index[new_num] = i

            self.nums.pop()
            del self.val_index[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()