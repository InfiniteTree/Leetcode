class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1, p2 = 1, 1
        while p2 < len(nums):
            if nums[p2] != nums[p2-1]:
                nums[p1] = nums[p2]
                p1+=1
            p2 += 1
        return p1
        