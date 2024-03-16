class Solution:
    def getNext(self, next_, s):
        j = 0 # j: the last index of the prefix
        next_[0] = 0
        for i in range(1, len(s)): # i: the last index of the postfix
            while j> 0 and s[i] != s[j]:
                j = next_[j-1]
            if s[i] == s[j]:
                j += 1
            next_[i] = j 

    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        next_t = [0] * len(needle)
        self.getNext(next_t, needle)
        j = 0
        for i in range(len(haystack)):
            # move backward
            while j>0 and haystack[i] != needle[j]:
                j = next_t[j-1]
            # move forward
            if haystack[i] == needle[j]:
                j += 1
            # end
            if j == len(needle):
                return i - len(needle) + 1
        return -1
