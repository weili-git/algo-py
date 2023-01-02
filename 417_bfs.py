class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        result = []
        # visited
        pacific = [[False for j in range(n)] for i in range(m)]
        atlantic = [[False for j in range(n)] for i in range(m)]
        for i in range(m):
            self.dfs(heights, pacific, i, 0)  # 左出发，pacific
            self.dfs(heights, atlantic, i, n-1)  # 下出发，atlantic

        for j in range(n):
            self.dfs(heights, pacific, 0, j)  # 上出发，pacific
            self.dfs(heights, atlantic, m-1, j)  # 右出发，atlantic

        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])

        return result

    def dfs(self, heights, visited, x, y):
        if visited[x][y]:
            return
        visited[x][y] = True

        for i, j in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            nextx = x + i
            nexty = y + j
            if nextx<0 or nextx>=len(heights) or nexty<0 or nexty>=len(heights[0]): # 越界
                continue
            if heights[x][y] > heights[nextx][nexty]: # 需要逆流
                continue
            self.dfs(heights, visited, nextx, nexty)

    


        

    
