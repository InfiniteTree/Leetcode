class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        cnt = [0] * (n+1) # Record the num of papers of each citations
        for c in citations:
            #if c>n:
            #    c = n
            cnt[min(c, n)] += 1 
        s = 0 # s represent the paper nums
        for i in range(n, -1, -1):
            s += cnt[i]
            if s >= i:
                return i
 