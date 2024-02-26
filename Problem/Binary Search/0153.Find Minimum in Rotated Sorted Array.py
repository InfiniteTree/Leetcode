class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        # [0, n-2] -> (-1, n-1)
        left = -1
        right = n-1
        while left + 1 < right:
            mid = (left+right) // 2
            if nums[mid] < nums[-1]:
                right = mid
            else:
                left = mid
        return nums[right]
