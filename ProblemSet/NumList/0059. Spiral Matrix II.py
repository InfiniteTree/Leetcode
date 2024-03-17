class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        l, t, r, b = 0, 0, n-1, n-1  # left, top, right, bottom
        num, tar = 1, n*n
        mat = [[0] * n for _ in range(n)]
        while num <= tar:
            for i in range(l, r+1): # from left to right
                mat[t][i] = num
                num += 1
            t += 1

            for i in range(t, b+1): # from top to bottom
                mat[i][r] = num
                num += 1
            r -= 1

            for i in range(r, l-1, -1): # from right to left
                mat[b][i] = num
                num += 1
            b -= 1

            for i in range(b, t-1, -1): # from bottom to top
                mat[i][l] = num
                num += 1
            l += 1
        return mat
