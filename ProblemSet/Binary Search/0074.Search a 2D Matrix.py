class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0,  n*m-1
        while left <= right:
            mid = (left+right) // 2
            x = matrix[mid//n][mid%n]
            if x == target:
                return True
            elif x > target:
                right = mid-1
            elif x < target:
                left = mid+1
        return False
        