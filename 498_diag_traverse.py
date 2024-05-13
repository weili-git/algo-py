class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = list()
        up_left = True
        i, j = 0, 0
        m, n = len(mat), len(mat[0])
        for k in range(m*n):
            res.append(mat[i][j])
            if up_left:
                if j==n-1: # right border
                    i += 1
                    up_left = False
                elif i==0: # up border
                    j += 1
                    up_left = False
                else:
                    i -= 1
                    j += 1
            else:
                if i==m-1:
                    j += 1
                    up_left = True
                elif j==0:
                    i += 1
                    up_left = True
                else:
                    i += 1
                    j -= 1
        return res
                


                    


