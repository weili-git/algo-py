"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        output = []
        while queue:
            tmp = []
            res = []
            for q in queue:
                tmp += q.children
                res.append(q.val)
            output.append(res)
            queue = tmp

        return output