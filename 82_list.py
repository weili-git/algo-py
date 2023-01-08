# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummyHead = dummy
        while head: # remove all duplications
            if head.next and head.val == head.next.val:
                tmp = head.next.next
                while tmp and tmp.val==head.val:
                    tmp = tmp.next
                head = tmp
            else:
                dummy.next = head
                dummy = dummy.next
                head = head.next
        dummy.next = None # 删除无用的后续节点，因为dummy的后续可能残存head的后续节点
        return dummyHead.next



