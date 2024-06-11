class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ptr1, ptr2 = len(g)-1, len(s)-1
        g.sort()
        s.sort()
        res = 0
        while ptr2 >= 0 and ptr1 >= 0:
            if s[ptr2] >= g[ptr1]:
                res += 1
                ptr2 -= 1
                ptr1 -= 1
            else:
                ptr1 -= 1
        return res
