class Solution:
    def isValid(self, s, start, end):
        # Case One
        if start > end or (s[start] == "0" and start != end):
            return False
        num = 0
        for i in range(start, end+1):
            # Case Two
            if not s[i].isdigit():
                return False
            # Case Three
            num = num * 10 + int(s[i])
            if num > 255:
                return False
        return True 

    def backtracking(self, s, startIdx, cnt, path, ret):
        if cnt == 3:
            if self.isValid(s, startIdx, len(s)-1):
                path += s[startIdx:]
                ret.append(path)
                return
        for i in range(startIdx, len(s)):
            if self.isValid(s, startIdx, i):
                sub = s[startIdx:i+1]
                self.backtracking(s, i+1, cnt+1, path+sub+".", ret) 

    def restoreIpAddresses(self, s: str) -> List[str]:
        ret = []
        path = ''
        self.backtracking(s, 0, 0, path, ret)
        return ret

