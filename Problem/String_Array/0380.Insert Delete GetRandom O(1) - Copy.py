class RandomizedSet:

    def __init__(self):
        self.hashmap = {} # val: idx
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.values:
            return False
        else:
            self.values.append(val)
            self.hashmap[val] = len(self.values) - 1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.values:
            return False
        else:
            idx = self.hashmap[val]
            temp = self.values[-1]
            self.values[idx] = temp # exchange the deleted element with the last element in the set
            self.hashmap[temp] = idx
            self.values.pop()
            del self.hashmap[val] 
            return True

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
