class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return nums1  
        end_idx = m+n-1
        while n>0 and m>0:
            if nums2[n-1] >= nums1[m-1]:
                nums1[end_idx] = nums2[n-1]
                end_idx -= 1
                n -= 1
            else:
                nums1[end_idx] = nums1[m-1]
                end_idx -= 1
                m -= 1
        if m == 0 and n>0:
        # some elements remained in nums2: all the elements in nums1 > the remained in nums2
            while n>0:
                nums1[end_idx] = nums2[n-1]
                end_idx -= 1
                n -= 1
        return nums1
