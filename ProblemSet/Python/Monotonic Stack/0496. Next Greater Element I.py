class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        hashMap = {}
        stack = [0]
        # Method 1: Skip the mapping part by using list.index, while it costs most time

        for num in nums2:
            if num <= stack[-1]:
                stack.append(num)
            else:
                while stack and num > stack[-1]:
                    hashMap[stack[-1]] = num
                    stack.pop()
                stack.append(num)
                
        for num in nums1:
            res.append(hashMap.get(num, -1))
        return res
