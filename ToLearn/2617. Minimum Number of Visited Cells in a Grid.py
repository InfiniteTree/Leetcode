class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        # dp[i][j]: the minimum steps to reach (i, j)
        m, n = len(grid), len(grid[0])

        col_heaps = [[] for _ in range(n)] # store (dis[i][k], i, k) 
        for i, row in enumerate(grid):
            row_h = []
            for j, (g, col_h) in enumerate(zip(row, col_heaps)):
                while row_h and row_h[0][1] < j:
                    heappop(row_h)
                while col_h and col_h[0][1] < i:
                    heappop(col_h)
                dp = inf if i or j else 1
                if row_h: dp = row_h[0][0] + 1
                if col_h: dp = min(dp, col_h[0][0]+1)
                if g and dp < inf:
                    heappush(row_h, (dp, g+j))
                    heappush(col_h, (dp, g+i))
        return dp if dp < inf else -1

'''
class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        # 向右向下 动态规划
        m = len(grid)
        n = len(grid[0])
        # 记忆化搜索
        # @cache
        # def dfs (i:int, j:int) -> int:
        #     if i == m -1 and j == n-1:
        #         return 1
        #     if grid[i][j] == 0:
        #         return inf
        #     ans = inf
        #     for index_i in range(1,grid[i][j]+1):
        #         if i + index_i <= m-1:
        #             ans = min(ans,dfs(i+index_i,j))
            
        #     for index_j in range(1,grid[i][j]+1):
        #         if j + index_j <= n-1:
        #             ans = min(ans,dfs(i,j+index_j))
        #     return ans +1
        # return dfs(0,0) if dfs(0,0) < inf else -1
        # 递推
        # dp = [[inf for _ in range(n)] for _ in range(m)]
        # dp[m-1][n-1] = 1
        # for i in range(m-1,-1,-1):
        #     for j in range(n-1,-1,-1):
        #         if grid[i][j] != 0:
        #             for index_i in range(1,grid[i][j]+1):
        #                 if i + index_i <= m-1:
        #                     dp[i][j] = min(dp[i][j],dp[i+index_i][j]+1)
        #             for index_j in range(1,grid[i][j]+1):
        #                 if j + index_j <= n-1:
        #                     dp[i][j] = min(dp[i][j],dp[i][j+index_j]+1)
        # return dp[0][0] if dp[0][0] < inf else -1
        # 线段树优化
        # 需要两棵线段树，横向纵向各一棵
        # 单点更新，区间查询
        t_d = [SegmentTree(m) for _ in range(n)]
        for i in range(m-1,-1,-1):
            t_r = SegmentTree(n)
            for j in range(n-1,-1,-1):
                if i == m-1 and j == n-1:
                    t_r.update(1,1,n, n, 1)
                    t_d[j].update(1,1,m, m, 1)
                else:
                    if grid[i][j] != 0:
                        f_r = inf
                        f_d = inf
                        if j < n-1:
                            f_r = t_r.query(1,1,n, j+1+1,min(grid[i][j] + j,n-1)+1) 
                            # print(f_r)
                        if i < m-1:
                            f_d = t_d[j].query(1,1,m,i+1+1,min(grid[i][j] + i,m-1)+1) 
                        res_v = min(f_d,f_r) + 1
                        # print(res_v,grid[i][j])
                        t_r.update(1,1,n,  j+1, res_v)
                        t_d[j].update(1,1,m, i+1, res_v)

        ans = t_d[0].query(1,1,m,1,1)
        return ans if ans < inf else -1


class SegmentTree:
    def __init__(self,cap:int):
        self.tree = [inf] * (4 * cap)
    def update(self,o: int, l: int, r: int, i: int, val: int) -> None:
        if l == r:
            self.tree[o] = val
            return
        m = (l + r) // 2
        if i <= m: self.update(o * 2, l, m, i, val)
        else: self.update(o * 2 + 1, m + 1, r, i, val)
        self.tree[o] = min(self.tree[o * 2], self.tree[o * 2 + 1])
    def query(self,o: int, l: int, r: int, L: int, R: int) -> int:  
        if L <= l and r <= R: return self.tree[o]
        res = inf
        m = (l + r) // 2
        if L <= m: res = self.query(o * 2, l, m, L, R)
        if R > m: res = min(res, self.query(o * 2 + 1, m + 1, r, L, R))
        return res
'''