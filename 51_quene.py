class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        board = [['.' for i in range(n)] for j in range(n)]
        self.backtrack(n, 0, board)
        return self.res
        
    def backtrack(self, n, row, board):
        if row==n:
            self.res.append(["".join(row) for row in board])
            return
        for col in range(n):
            if self.isValid(row, col, board, n):
                board[row][col] = "Q"
                self.backtrack(n, row+1, board)
                board[row][col] = "."


    def isValid(self, row, col, board, n):
        # check column
        for i in range(row):
            if board[i][col]=="Q":
                return False
        # check 45 degree
        i = row - 1
        j = col - 1
        while i>=0 and j>=0:
            if board[i][j]=="Q":
                return False
            i -= 1
            j -= 1
        # check 135 degree
        i = row - 1
        j = col + 1
        while i>=0 and j<n:
            if board[i][j]=="Q":
                return False
            i -= 1
            j += 1
        return True
        
