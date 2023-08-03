# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution: # divide and conquer
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if root==p or root==q:
            return root
        first = self.lowestCommonAncestor(root.left, p, q)
        second = self.lowestCommonAncestor(root.right, p, q)
        if first and second:
            return root
        if first:
            return first
        if second:
            return second
        return None