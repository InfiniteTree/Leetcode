class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k, m, n):
            idx1, idx2 = 0, 0
            while True:
                # Special condiction
                if idx1 == m: 
                    return nums2[idx2+k-1]
                if idx2 == n:
                    return nums1[idx1+k-1]
                if k == 1:
                    return min(nums1[idx1], nums2[idx2])

                
                # Normal condicion
                newidx1 = min(idx1 + k//2 -1, m-1)
                newidx2 = min(idx2 + k//2 -1, n-1)
                pivot1, pivot2 = nums1[newidx1], nums2[newidx2]
                # update
                if pivot1 <= pivot2:
                    k -= newidx1 - idx1 + 1
                    idx1 = newidx1 + 1
                else:
                    k -= newidx2 - idx2 + 1
                    idx2 = newidx2 + 1

        m, n = len(nums1), len(nums2)
        total = m + n
        if total % 2 == 1:
            return getKthElement((total+1)//2, m, n)
        else:
            return  (getKthElement(total//2, m, n) + getKthElement(total//2 + 1, m, n)) / 2

    