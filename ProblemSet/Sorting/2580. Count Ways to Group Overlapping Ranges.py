import math
class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        ranges.sort(key=lambda x:x[0])
        n, max_r = 0, -inf
        for l, r in ranges:
            if l > max_r:
                n += 1
            max_r = max(max_r, r)
        return pow(2, n, mod)
        '''
        merge_ranges = [ranges[0]]
        for i in range(1, len(ranges)):
            if ranges[i][0] <= merge_ranges[-1][1]:
                front = merge_ranges[-1][0]
                back = max(merge_ranges[-1][1], ranges[i][1])
                merge_ranges.pop()
                merge_ranges.append([front,back])
            else:
                merge_ranges.append([ranges[i][0], ranges[i][1]])
        n = len(merge_ranges)
        return pow(2, n, mod)
        '''

