class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        self.grid = grid
        return self.get_subtree(0, 0, n)

    def get_subtree(self, i, j, n):
        # if n==1:
        #     return Node(1, self.grid[i][j])
        if all(self.grid[x][y] == self.grid[i][j] for x in range(i, i+n) for y in range(j, j+n)):
            return Node(self.grid[i][j]==1, True)
        
        # or 
        # 使用前缀和，记录区域的和，方便判断是否全为1或0

        topLeft = self.get_subtree(i, j, n//2)
        topRight = self.get_subtree(i, j+n//2, n//2)
        bottomLeft = self.get_subtree(i+n//2, j, n//2)
        bottomRight = self.get_subtree(i+n//2, j+n//2, n//2)

        if topLeft==topRight and topLeft==bottomLeft and topLeft==bottomRight:
            return topLeft
        else:
            return Node(1, 0, topLeft, topRight, bottomLeft, bottomRight)
        

# T(n)=4T(n/2)+O(n^2)
# O(n^2logn)
# 空间复杂度：O(logn) 递归栈空间

# 优化后

# T(n)=4T(n/2)+O(1)
# O(n^2)
# 空间复杂度：O(n^2)

