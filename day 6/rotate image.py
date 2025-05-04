class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n % 2 == 0:
            limit = n // 2
            odd = False
        else:
            limit = n // 2 + 1
            odd = True
        for j in range(limit):
            for i in range(limit):
                if odd and j == limit - 1 and i != limit - 1:
                    continue
                self.permute(matrix, i, j)
    
    def permute(self, matrix, x, y):
        n = len(matrix)
        deleted_value = matrix[y][x]
        for _ in range(4):
            new_x = n - y - 1
            new_y = x
            value = matrix[new_y][new_x]
            matrix[new_y][new_x] = deleted_value
            deleted_value = value
            x = new_x
            y = new_y
        
