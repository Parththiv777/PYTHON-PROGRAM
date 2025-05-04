class Solution(object):
    def spiralOrder(self, mat):
        col = len(mat[0])
        row = len(mat)
        left, top = 0, 0
        right, bottom = col-1, row-1
        
        op = []
        while left <= right and top <= bottom:
            for i in range(left,right+1):
                op.append(mat[top][i])
            top += 1

            for j in range(top,bottom+1):
                op.append(mat[j][right])
            right -= 1

            if (top <= bottom):
                for k in range(right,left-1,-1):
                    op.append(mat[bottom][k])
            bottom -= 1

            if (left <= right):
                for l in range(bottom,top-1,-1):
                    op.append(mat[l][left])
            left += 1

        return op
        
