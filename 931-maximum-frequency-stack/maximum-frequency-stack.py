class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        val_freq = self.freq[val] + 1
        self.freq[val] = val_freq
        self.group[val_freq].append(val)
        self.max_freq = max(self.max_freq, val_freq)

    def pop(self) -> int:
        most_freq_val = self.group[self.max_freq].pop()
        self.freq[most_freq_val] -= 1
        if len(self.group[self.max_freq]) == 0:
            self.max_freq -= 1
        return most_freq_val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()