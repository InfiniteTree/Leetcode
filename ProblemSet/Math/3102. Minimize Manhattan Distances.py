from sortedcontainers import SortedList
class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        # Chebyshev Distance
        # max(|x1-x2|+|y1-y2|) = max(max(x1'-x2', y1'-y2')) = max(max(x1')-min(x2'), max(y1')- min(y2'))
        '''
        xs = SortedList()
        ys = SortedList()
        for x, y in points:
            xs.add(x+y)
            ys.add(y-x)
        
        ans = inf
        for x, y in points:
            x, y = x+y, y-x
            xs.remove(x)
            ys.remove(y)
            ans = min(ans, max(xs[-1] - xs[0], ys[-1] - ys[0]))
            xs.add(x)
            ys.add(y)
        return ans
        '''
        # Optimization
        xs = [x + y for x, y in points]
        ys = [y - x for x, y in points]
        max_x1, max_x2 = nlargest(2, xs)   # largest xs and second largest xs
        min_x1, min_x2 = nsmallest(2, xs)  # smallest xs and second smallest xs
        max_y1, max_y2 = nlargest(2, ys)   # largest ys and second largest ys
        min_y1, min_y2 = nsmallest(2, ys)  # smallest ys and second smallest ys
        idx = [xs.index(max_x1), xs.index(min_x1), ys.index(max_y1), ys.index(min_y1)]

        ans = inf
        for i in idx:
            dx = (max_x2 if i == idx[0] else max_x1) - (min_x2 if i == idx[1] else min_x1)
            dy = (max_y2 if i == idx[2] else max_y1) - (min_y2 if i == idx[3] else min_y1)
            ans = min(ans, max(dx, dy))
        return ans
