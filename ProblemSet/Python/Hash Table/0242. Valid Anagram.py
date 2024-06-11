from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt1 = Counter(s)
        cnt2 = Counter(t)
        return cnt1 == cnt2
        