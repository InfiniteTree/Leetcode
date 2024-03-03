class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        ptr1, ptr2 = 0, 0
        while ptr1 <= len(s) - 1 and ptr2 <= len(t)-1:
            if s[ptr1] == t[ptr2]:
                ptr1 += 1
                ptr2 += 1
            else:
                ptr2 += 1
        if ptr1 == len(s):
            return True
        else:
            return False
