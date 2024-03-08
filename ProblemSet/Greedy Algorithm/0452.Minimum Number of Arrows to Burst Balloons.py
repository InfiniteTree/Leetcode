class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        #print(points)
        maximum = float("-inf")
        arrow = 0
        for x in points:
            if x[0] > maximum:
                maximum = x[1]
                arrow += 1
        return arrow