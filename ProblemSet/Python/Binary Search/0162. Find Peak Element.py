class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # [0, n-2] => (-1, n-1)
        n = len(nums)
        left = -1
        right = n-1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid+1]:
                left = mid
            else:
                right = mid
            #print(left, right)
        return right
