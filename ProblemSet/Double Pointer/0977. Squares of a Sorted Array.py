class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        l, r = 0, len(nums)-1
        while l <= r:
            if abs(nums[l]) < abs(nums[r]):
                res.append(nums[r]**2)
                r -= 1
            else:
                res.append(nums[l]**2)
                l += 1
        return res[::-1]
        ### return sorted([x**2 for x in nums]) # Brute force method
