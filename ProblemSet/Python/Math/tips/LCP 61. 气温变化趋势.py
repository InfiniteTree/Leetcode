class Solution:
    def temperatureTrend(self, temperatureA: List[int], temperatureB: List[int]) -> int:
        res, cnt = 0, 0
        '''
        for i in range(1, len(temperatureA)):
            if (temperatureA[i] == temperatureA[i-1] and temperatureB[i] == temperatureB[i-1]) or ((temperatureA[i]-temperatureA[i-1])*(temperatureB[i]-temperatureB[i-1])>0):
                cnt += 1
                res = max(res, cnt)
            else:
                cnt = 0
        '''
        # Simplification
        for (a1, b1), (a2, b2) in pairwise(zip(temperatureA, temperatureB)):
            if (a1 > a2) - (a1 < a2) == (b1 > b2) - (b1 < b2):
                cnt += 1
                res = max(cnt, res)
            else:
                cnt = 0
        return res
        