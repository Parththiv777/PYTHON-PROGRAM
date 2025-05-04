class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for i in range(n)] for j in range(n)]
        curnum = 1
        left = 0
        top = 0
        right = n-1
        bottom = n-1
        while (curnum <= n**2):
            for j in range(left, right+1):
                matrix[top][j] = curnum
                curnum += 1
            top += 1
            for i in range(top, bottom+1):
                matrix[i][right] = curnum
                curnum += 1
            right -= 1
            for j in range(right, left-1, -1):
                matrix[bottom][j] = curnum
                curnum += 1
            bottom -= 1
            for i in range(bottom, top-1, -1):
                matrix[i][left] = curnum
                curnum += 1
            left += 1
        return matrix
