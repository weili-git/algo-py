class Solution:
    # def getMoneyAmount(self, n: int) -> int:
    #     # f[1][n] = x + max(f[1][x-1], f[x+1][n]) # guarantee
    #     # min max problem
    #     f = [[0]*(n+1) for _ in range(n+1)]

    #     # f[i][<=i] = 0 是已经计算好的子问题
    #     for i in range(n-1,0,-1):
    #         for j in range(i+1, n+1): # f[i][j] = 0 if i>=j
    #             f[i][j] = j + f[i][j-1]
    #             for k in range(i,j):
    #                 f[i][j] = min(f[i][j], k+max(f[i][k-1], f[k+1][j]))
    #     return f[1][n]

    def getMoneyAmount(self, n: int) -> int:
        f = [[0]*(n+1) for _ in range(n+1)]

        for i in range(1,n):
            f[i][i+1] = i
        for d in range(2, n):
            for i in range(1, n-d+1):
                f[i][i+d] = min(i+f[i+1][i+d], i+d+f[i][i+d-1]) # two side
                for j in range(i+1, i+d):
                    f[i][i+d] = min(f[i][i+d], j+max(f[i][j-1], f[j+1][i+d]))
        return f[1][n]