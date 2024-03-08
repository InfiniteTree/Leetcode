class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # derivative: True for the positive differences and False for the negatie difference before
        res = 1
        if len(nums) < 2:
            return len(nums)
        derivative = None
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                if derivative is None or not derivative: # the previous time is negative derivative
                    derivative = True
                    res += 1
            elif nums[i] < nums[i-1]:
                if derivative is None or derivative: # the previous time is positive derivative
                    derivative = False
                    res += 1
        return res
