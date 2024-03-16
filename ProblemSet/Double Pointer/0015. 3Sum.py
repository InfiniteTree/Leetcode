class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # i < j < k
        n = len(nums)
        nums.sort()
        ret = []
        for i in range(n-2):
            x = nums[i]
            if i>0 and x == nums[i-1]:
                continue # jump to the next for duplicate triplets
            else:
                left = i+1
                right = n-1
                while left < right:
                    if x == -(nums[left] + nums[right]):
                        ret.append([x, nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1

                    elif x > -(nums[left] + nums[right]):
                        right -= 1
                    else: 
                        left += 1
        return ret
