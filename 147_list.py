# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = head
        while cur:
            next = cur.next
            cur.next = None
            self.insert(dummy, cur)
            cur = next
        return dummy.next

    def insert(self, dummy, node):
        if not dummy.next:
            dummy.next = node
            return
        if dummy.next.val >= node.val:
            node.next = dummy.next
            dummy.next = node
            return
        prev = None
        pp = dummy
        while pp.next and pp.next.val < node.val:
            prev = pp.next
            pp = pp.next
        if pp.next:
            node.next = pp.next
            prev.next = node
        else:
            pp.next = node