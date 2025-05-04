class Solution(object):
    def DFS(self, board, word, col, row, idx):        
        # base case 1: If the idx is greater or equal to the number of letters then it means 
        # that we alread found the word and so we return True 
        if idx >= len(word):
            return True 
        
        # base case 2: If we are out of bound or if the letter at indx does not match 
        # return False
        if (col<0 or row<0 or row>=len(board) or col >= len(board[0]) or board[row][col] != word[idx]):
            return False 
        
        letter = board[row][col]
        board[row][col] = ""
        # recurssive case: if the letter exists in the surroundings letters then pick 
        
        # check for the four neighbors 
        found = (   #neighor is left or right 
                    self.DFS(board, word, col, row+1, idx+1) 
                    or self.DFS(board, word, col, row-1, idx+1) 
                    #neighbor is up or down 
                    or self.DFS(board, word, col+1, row, idx+1) 
                    or self.DFS(board, word, col-1, row, idx+1) )
        
        # reset the board for other searches 
        board[row][col] = letter 

        return found 

   
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        #get the total number or rows and the total number or columns 
        ROWS, COLS = len(board), len(board[0])
        #double for-loop to iterate over every single index in the board (Brute Force)
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == word[0]: 
                    if (self.DFS(board, word, col, row, 0)): 
                        return True

        return False 
