class Solution:
    def is_subseq(self, str1: str, str2: str) -> bool:
        ptr_i,ptr_j = 0, 0
        while ptr_i <= len(str1)-1 and ptr_j <= len(str2)-1:
            if str1[ptr_i] == str2[ptr_j]:
                ptr_i += 1
            ptr_j += 1
        return ptr_i == len(str1)

    def findLUSlength(self, strs: List[str]) -> int:
        res, n = -1, len(strs)
        for i in range(n):
            flag = True # Check whether the strs[i] is a subsequence of strs[j]
            for j in range(n):
                if i!= j and self.is_subseq(strs[i], strs[j]):
                    flag = False
                    break
            if flag:
                res = max(res, len(strs[i]))
        return res
