class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLowBound(nums, target):
            left = 0
            right = len(nums)-1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid+1
                elif nums[mid] >= target:
                    right = mid-1
            return left
        
        if len(nums) == 0:
            return [-1, -1]
        start = findLowBound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = findLowBound(nums, target+1) - 1
        return [start, end]
