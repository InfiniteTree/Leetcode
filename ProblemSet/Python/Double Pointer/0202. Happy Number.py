class Solution:
    def isHappy(self, n: int) -> bool:
        s = n # a random number that is larger than 10
        record = set()
        while s != 1:
            s = sum(int(num) ** 2 for num in str(s))
            if s in record:
                return False
            record.add(s)
        return True
