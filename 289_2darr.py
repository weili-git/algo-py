class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        next = [[[] for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                next[i][j] = self.get_next(board, i, j, m, n)
        
        # modify the original matrix
        for i in range(m):
            for j in range(n):
                board[i][j] = next[i][j]

    def get_next(self, board, i, j, m, n):
        cnt = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x==0 and y==0:
                    continue
                if i+x>=0 and i+x<m and j+y>=0 and j+y<n and board[i+x][j+y]==1:
                    cnt = cnt + 1
        if board[i][j]==1:
            if cnt in [2, 3]:
                return 1
            else:
                return 0
        else:
            if cnt==3:
                return 1
            else:
                return 0