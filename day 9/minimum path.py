class Solution:
    def recur(self, grid, row, col):
        if row == 0 and col == 0:
            return grid[0][0]
        if col == 0:
            l = self.recur(grid, row - 1, col)
        else:
            l = self.recur(grid, row, col - 1)
        if row == 0:
            t = self.recur(grid, row, col - 1)
        else:
            t = self.recur(grid, row - 1, col)
        return min(l, t) + grid[row][col]

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid) - 1
        col = len(grid[0]) - 1
        return self.recur(grid, row, col)
    
