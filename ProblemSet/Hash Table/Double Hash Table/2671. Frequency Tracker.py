from collections import defaultdict
class FrequencyTracker:
    def __init__(self):
        self.nums = defaultdict(int)
        self.freq = defaultdict(int)

    def add(self, number: int, delta=1) -> None:
        if self.nums[number]:
            self.freq[self.nums[number]] -= 1
            self.nums[number] += delta
            self.freq[self.nums[number]] += 1
        else:
            self.nums[number] = 1
            self.freq[self.nums[number]] += 1

    def deleteOne(self, number: int) -> None:
        if self.nums[number]:
            self.add(number,-1)

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] > 0

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)