# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        
        slow = head
        fast = head
        while fast.next and fast.next.next: # 1. find middle
            slow = slow.next
            fast = fast.next.next

        needReverser = slow.next # 2. reverse
        slow.next = None
        needReverser = reverse(needReverser)

        cur = head
        while cur and needReverser: # 3. traverse
            curSecond = needReverser
            needReverser = needReverser.next
            nextCur = cur.next
            curSecond.next = cur.next
            cur.next = curSecond

            cur = nextCur
            # cur_n = cur.next
            # rev_n = needReverser.next
            # cur.next = needReverser
            # needReverser.next = cur_n
            # cur = cur_n
            # needReverser = Rev_n


    def reverse(self, head):
        p1 = None
        p2 = head
        p3 = p2
        while p2:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3
        return p1