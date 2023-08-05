class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.sum_mat = matrix.copy()
        for i in range(m):
            for j in range(n):
                if i>0 and j>0:
                    self.sum_mat[i][j] += self.sum_mat[i-1][j] + self.sum_mat[i][j-1] - self.sum_mat[i-1][j-1]
                elif i>0:
                    self.sum_mat[i][j] += self.sum_mat[i-1][j]
                elif j>0:
                    self.sum_mat[i][j] += self.sum_mat[i][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 >0 and col1>0:
            return self.sum_mat[row2][col2] - self.sum_mat[row1-1][col2] - self.sum_mat[row2][col1-1] + self.sum_mat[row1-1][col1-1]
        elif row1 >0:
            return self.sum_mat[row2][col2] - self.sum_mat[row1-1][col2]
        elif col1 >0:
            return self.sum_mat[row2][col2] - self.sum_mat[row2][col1-1]
        else:
            return self.sum_mat[row2][col2]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)