class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        '''
        if len(matches) == 1:
            return [[matches[0][0]], [matches[0][1]]]
        matches.sort(key = lambda x:x[1])
        ans = [[],[]]
        # ans[0]
        win = set()
        lose = set()
        for match in matches:
            win.add(match[0])
            lose.add(match[1])
        ans[0] = list(win - lose)
        ans[0].sort()

        # ans[1]
        if matches[0][1] != matches[1][1]:
            ans[1].append(matches[0][1])
        for i in range(1, len(matches)-1):
            if matches[i][1] != matches[i-1][1] and matches[i][1] != matches[i+1][1]: # lose only one match
                ans[1].append(matches[i][1])
        if matches[-1][1] != matches[-2][1]:
            ans[1].append(matches[-1][1])
        return ans
        '''
        players = set(x for m in matches for x in m)
        loss_cnt = Counter(loser for _, loser in matches)
        
        return [sorted(x for x in players if x not in loss_cnt),
                sorted(x for x, c in loss_cnt.items() if c == 1)]
