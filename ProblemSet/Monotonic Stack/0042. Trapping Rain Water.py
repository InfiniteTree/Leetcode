class Solution:
    def trap(self, height: List[int]) -> int:
        ret = 0
        left, right = 0, len(height)-1
        pre_max, suf_max = 0, 0
        while left < right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            if pre_max < suf_max:
                ret += pre_max - height[left]
                left += 1
            else:
                ret += suf_max - height[right]
                right -= 1
        return ret
'''''
# Motonic Stack Method
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        stack = [0]
        for i in range(1, len(height)):
            if height[i] <= height[stack[-1]]:
                stack.append(i)
            else:
                while stack and height[i] > height[stack[-1]]:
                    mid = stack.pop()
                    if stack:
                        h = min(height[i], height[stack[-1]]) - height[mid]
                        w = i - stack[-1] - 1
                        res += h * w
                stack.append(i)
        return res
'''
        