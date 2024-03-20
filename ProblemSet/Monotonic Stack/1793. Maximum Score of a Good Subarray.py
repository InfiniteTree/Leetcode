class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        nums.append(0)
        st = []
        res = 0
        for r, num in enumerate(nums):
            while st and nums[st[-1]] > num:
                mid = st.pop()
                l = st[-1] if st else -1
                if l < k < r:
                    width = r - l - 1
                    height = nums[mid]
                    res = max(res, width * height)
            st.append(r)
        return res
       