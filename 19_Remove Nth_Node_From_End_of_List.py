# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        pnt1, pnt2 = dummy, head
        for _ in range(n):
            pnt2 = pnt2.next

        while pnt2:
            pnt1, pnt2 = pnt1.next, pnt2.next
        
        pnt1.next = pnt1.next.next
        return dummy.next
