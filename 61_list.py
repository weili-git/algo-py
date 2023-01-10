# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if (not head.next) or k==0:
            return head
        dummy = ListNode(0)
        dummy.next = head
        slow = head
        fast = head
        kk = 0
        i = 0
        while i<k:
            if fast.next:
                fast = fast.next
                kk += 1
                i += 1
            else:
                fast = head
                i = 0
                k = k % (kk+1)
                if k==0:
                    return head
        while fast.next:
            slow = slow.next
            fast = fast.next
        tmp = slow.next
        slow.next = None
        fast.next = dummy.next
        return tmp
