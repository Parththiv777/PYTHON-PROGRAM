class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Loop through each element and check whether it's valid
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    if not self.isValid(board, i, j):
                        return False
        return True

    # Given a position, return whether the element is valid 
    def isValid(self, board, i, j):
        # Check rows
        for index in range(j + 1, len(board)):
            if board[i][index] == board[i][j]:
                return False
        # Check cols
        for index in range(i + 1, len(board[0])):
            if board[index][j] == board[i][j]:
                return False
        # Check tiles
        startRow = i - (i % 3)
        endRow = startRow + 3
        startCol = j - (j % 3)
        endCol = startCol + 3
        for outer in range(startRow, endRow):
            for inner in range(startCol, endCol):
                if board[outer][inner] == board[i][j] and (outer != i and inner != j):
                    return False
        return True    
