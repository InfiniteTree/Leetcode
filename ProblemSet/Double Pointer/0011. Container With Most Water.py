class Solution:
    def maxArea(self, height: List[int]) -> int:
        ret = 0
        ptr_l, ptr_r = 0, len(height)-1
        while ptr_l < ptr_r:
            area = abs(ptr_l - ptr_r) * min(height[ptr_l], height[ptr_r])
            if area >= ret:
                ret = area
            if height[ptr_l] < height[ptr_r]:
                ptr_l += 1
            else: 
                ptr_r -= 1
        return ret