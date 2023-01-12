# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        elif not head.next:
            return TreeNode(head.val)
        pre = head
        p = pre.next
        q = p.next
        while q and q.next: # 寻找中点
            pre = pre.next
            p = pre.next
            q = q.next.next

        pre.next = None
        root = TreeNode(p.val) # 中点作为树根
        root.left = self.sortedListToBST(head) # 子问题1
        root.right = self.sortedListToBST(p.next) # 子问题2
        return root