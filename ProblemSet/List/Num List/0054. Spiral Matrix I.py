class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        l, t, r, b = 0, 0, n-1, m-1  # left, top, right, bottom
        res = []
        while len(res) < m*n:
            for i in range(l, r+1): # from left to right
                res.append(matrix[t][i]) 
            t += 1
            if t > b:
                break

            for i in range(t, b+1): # from top to bottom
                res.append(matrix[i][r]) 
            r -= 1
            if r < l:
                break

            for i in range(r, l-1, -1): # from right to left
                res.append(matrix[b][i]) 
            b -= 1
            if b < t:
                break

            for i in range(b, t-1, -1): # from bottom to top
                res.append(matrix[i][l]) 
            l += 1
            if l > r:
                break
        return res
