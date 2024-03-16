class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = [0]
        zero = [0]
        heights.insert(0,0)
        heights.append(0)
        
        for i in range(1, len(heights)):
            if heights[i] >= heights[stack[-1]]:
                stack.append(i)
            else:
                s = 0
                h = inf
                while stack and heights[i] < heights[stack[-1]]:
                    cur_height = heights[stack.pop()]
                    if stack:
                        h = min(h, cur_height)
                        w = i - stack[-1] - 1
                        s = max(s, h * w)
                stack.append(i)
                res = max(res, s)
        return res
