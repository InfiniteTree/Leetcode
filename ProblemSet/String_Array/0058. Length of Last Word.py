class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cnt = 0
        flag = False
        for i in range(len(s)-1, -1, -1):
            if s[i] == " " and not flag:
                continue
            if s[i] != " " and not flag:
                flag = True
            if s[i] == " " and flag:
                return cnt
            cnt += 1
        return cnt
