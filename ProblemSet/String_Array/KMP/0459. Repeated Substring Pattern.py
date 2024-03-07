class Solution:
    def getNext(self, nxt, s):
        j = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = nxt[j-1]
            if s[i] == s[j]:
                j += 1
            nxt[i] = j
            
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 0:
            return False
        nxt_t = [0] * len(s)
        self.getNext(nxt_t, s)
        if nxt_t[-1] != 0 and len(s) % (len(s)-nxt_t[-1]) == 0:
            return True
        return False
        