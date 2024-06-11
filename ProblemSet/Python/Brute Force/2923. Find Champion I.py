class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        # Method 1
        '''
        for i, row in enumerate(grid):
            if sum(row) == len(grid) - 1:
                return i
        # Method 2
        '''
        #print(list(zip(*grid)))
        '''
        for j, col in enumerate(zip(*grid)):
            if 1 not in col:
                return j
        '''
        # Method 3
        ans = 0
        for i, row in enumerate(grid):
            if row[ans]:
                ans = i
        return ans