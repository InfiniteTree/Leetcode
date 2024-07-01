class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        n = len(values)
        g = [[] for _ in range(n)]
        for x, y, t in edges:
            g[x].append((y, t))
            g[y].append((x, t))
        
        # Dijkstra 
        dis = [inf] * n         
        dis[0] = 0
        h = [(0, 0)]
        while h:
            dx, x = heappop(h)
            if dx > dis[x]:  # x exist in the heap
                continue
            for y, d in g[x]:
                new_dis = dx + d
                if new_dis < dis[y]:
                    dis[y] = new_dis  # update the shortest path of the neighbour of x
                    heappush(h, (new_dis, y))

        def dfs(x: int, sum_t: int, sum_val: int) -> None:
            if x == 0:
                nonlocal ans
                ans = max(ans, sum_val)
            
            for y, t in g[x]:
                if sum_t + t + dis[y] > maxTime:
                    continue
                if vis[y]:
                    dfs(y, sum_t+t, sum_val)
                else:
                    vis[y] = True
                    dfs(y, sum_t+t, sum_val+values[y])
                    vis[y] = False
        ans = 0
        vis = [False] * n
        vis[0] = True
        dfs(0, 0, values[0])
        return ans
            