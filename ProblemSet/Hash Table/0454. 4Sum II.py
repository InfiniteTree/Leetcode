class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashMap = dict()
        for n1 in nums1:
            for n2 in nums2:
                key = n1+n2
                if key in hashMap:
                    hashMap[key] += 1
                else:
                    hashMap[key] = 1
        res = 0
        for n3 in nums3:
            for n4 in nums4:
                key = 0 - n3 - n4
                if key in hashMap:
                    res += hashMap[key]
        return res
                