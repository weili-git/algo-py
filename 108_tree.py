# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        res = []
        stack = [root]
        while stack:
            tmp = []
            stack_next = []
            for node in stack:
                tmp.append(node.val)

                if node.left:
                    stack_next.append(node.left)
                if node.right:
                    stack_next.append(node.right)

            res.append(tmp)
            stack = stack_next
        res.reverse()
        return res