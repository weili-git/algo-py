# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head
        dummy = head.next
        p1, p2 = head, head.next
        while p2 and p2.next:
            p1.next = p2.next
            p2.next = p2.next.next
            p1 = p1.next
            p2 = p2.next
        p1.next = dummy
        return head
        # just like reverse a list