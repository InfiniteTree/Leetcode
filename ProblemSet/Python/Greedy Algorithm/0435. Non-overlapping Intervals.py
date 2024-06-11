class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        #print(intervals)
        res = 0
        maximum = intervals[0][1]  # record the most right boundary
        for i in range(1, len(intervals)):
            if intervals[i][0] < maximum:
                res += 1
                maximum = min(maximum, intervals[i][1])
            else:
                maximum = max(maximum, intervals[i][1])
        return res
