class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1, p2 = 0, 0
        while p2 <= len(nums)-1:
            if nums[p2] != 0:
                nums[p1] = nums[p2]
                p1 += 1
            p2 += 1
        
        for i in range(p1, len(nums)):
            nums[i] = 0
