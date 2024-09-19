class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        vis = [[False]*n for j in range(m) ]
        cnt = 0
        for i in range(m):
            for j in range(n):
                if (not vis[i][j]) and board[i][j]=="X":
                    vis[i][j] = True
                    cnt += 1
                    if j+1<n and board[i][j+1]=="X": # horizontal
                        for k in range(j+1, n):
                            if board[i][k] == "X":
                                vis[i][k] = True
                            else:
                                break
                    elif i+1<m and board[i+1][j]=="X": # vertical
                        for k in range(i+1, m):
                            if board[k][j] == "X":
                                vis[k][j] = True
                            else:
                                break
        return cnt
        # 14min