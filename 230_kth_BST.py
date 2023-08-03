# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        prev = []
        node = root
        while node.left:
            prev.append(node)
            node = node.left
        # now node is the smallest
        for i in range(k-1):
            if node.right:
                node = node.right
                while node.left:
                    prev.append(node)
                    node = node.left
            else:
                node = prev.pop()
        return node.val
