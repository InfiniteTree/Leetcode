class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        s = sum(apple)
        res = 0
        capacity.sort()
        for i in range(len(capacity)-1, -1, -1):
            s -= capacity[i]
            res += 1
            if s <= 0:
                break
        return res
    