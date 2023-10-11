# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 不会做的时候，不妨考虑一下分治算法，假设子树已经满足条件
        self.max = 0
        self.dfs(root)
        return self.max
        
    def dfs(self, root):
        if root.left is None and root.right is None:
            return 0
        leftSize = 0 if root.left is None else self.dfs(root.left) + 1
        rightSize = 0 if root.right is None else self.dfs(root.right) + 1
        self.max = max(self.max, leftSize + rightSize)
        return max(leftSize, rightSize)