# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ld = self.getDepth(root.left)
        rd = self.getDepth(root.right)
        if ld==rd:
            return (1<<ld) + self.countNodes(root.right)
            # 1(根节点) + (1 << ld)-1(左完全左子树节点数) + 右子树节点数量
        else:
            return (1<<rd) + self.countNodes(root.left)
            # 1(根节点) + (1 << rd)-1(右完全右子树节点数) + 左子树节点数量
        
    def getDepth(self, node):
        depth = 0
        while node:
            depth += 1
            node = node.left
        return depth