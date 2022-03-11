# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        target = head
        prev = None
        while target:
            next = target.next
            target.next = prev
            prev, target = target, next
        
        return prev