class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {}
        for i, char in enumerate(s):
            last_idx[char] = i
        #print(last_idx)
        l, r = 0, 0
        res = []
        for i in range(len(s)):
            r = max(r, last_idx[s[i]])
            if i == r: # reach the a most right last_idx
                res.append(r-l+1)
                l = i+1
        return res
                