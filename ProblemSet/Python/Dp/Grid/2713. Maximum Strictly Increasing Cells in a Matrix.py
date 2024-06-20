class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        # Store the pos for calculate the row_max and col_max first
        # to avoid the repeated operation on the dp
        g = defaultdict(list)
        for i, row in enumerate(mat):
            for j, x in enumerate(row):
                g[x].append((i,j)) 
        
        row_max = [0] * len(mat)
        col_max = [0] * len(mat[0])
        for _, pos in sorted(g.items(), key=lambda t:t[0]):
            dp = [max(row_max[i], col_max[j]) + 1 for i, j in pos]
            for (i, j), dp_x in zip(pos, dp):
                row_max[i] = max(row_max[i], dp_x)
                col_max[j] = max(col_max[j], dp_x)
        return max(row_max)
