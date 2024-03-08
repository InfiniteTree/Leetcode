class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        #print(intervals)
        res = [intervals[0]]
        j = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[j][1]:
                #print(res)
                temp = res.pop()
                res.append([temp[0],max(temp[1],intervals[i][1])])
                continue
            res.append(intervals[i])
            j += 1     
        return res
