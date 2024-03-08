class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True, key=abs)
        ptr = 0
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1
        if k%2 == 1:
            nums[-1] = -nums[-1]
        
        #print(nums)
        return sum(nums)
