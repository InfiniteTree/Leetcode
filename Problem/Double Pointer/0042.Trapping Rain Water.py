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
        