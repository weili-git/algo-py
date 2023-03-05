# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        stack = [root]
        flag = True
        while stack:
            stack_next = []
            tmp = []
            while stack:
                node = stack.pop()
                tmp.append(node.val)
                if flag:
                    if node.left:
                        stack_next.append(node.left)
                    if node.right:
                        stack_next.append(node.right)
                else:
                    if node.right:
                        stack_next.append(node.right)
                    if node.left:
                        stack_next.append(node.left)
            flag = not flag
            res.append(tmp)
            stack = stack_next
        return res