# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        list1 = []
        pointer1 = pointer2 = ListNode()
        for n in lists:
            while n:
                list1.append(n)
                n = n.next
        list1.sort(key=lambda x: x.val) 
        for x in list1:
            pointer1.next = x
            pointer1 = pointer1.next
        return pointer2.next
      
