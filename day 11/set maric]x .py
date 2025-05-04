class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        lines, positions = self.find_zeros(matrix)
        for line in lines:
            matrix[line] = [0 for i in range(len(matrix[0]))]
        for position in positions:
            for line in matrix:
                line[position] = 0
    
    def find_zeros(self, matrix):
        lines = []
        positions = []
        for i in range(len(matrix)):
            if 0 in matrix[i]:
                lines.append(i)
                for j in range(len(matrix[i])):
                    if matrix[i][j] == 0:
                        positions.append(j)
        return lines, positions

        
