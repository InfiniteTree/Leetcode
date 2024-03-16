from sortedcontainers import SortedList
class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        ans = []
        stl = SortedList((v, i) for i, v in enumerate(nums)) # Maintain a sorted list to record the left sorted nums
        #print(stl)
        visit = [False] * n # Record whether the element has been visited
        total = sum(nums)
        for i, k in queries:
            #print(i, k)
            if not visit[i]: # The first step
                total -= nums[i]
                visit[i] = True
            for _ in range(k): # The second step
                if len(stl) == 0: 
                    break
                while stl and visit[stl[0][1]]:
                    stl.pop(0) # pop the element that has been visited
                if stl:
                    x, i = stl.pop(0)
                    total -= x
                    visit[i] = True
            ans.append(total)
        return ans
    