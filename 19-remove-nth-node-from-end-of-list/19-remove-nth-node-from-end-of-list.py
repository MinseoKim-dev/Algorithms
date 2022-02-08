# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        target = head
        length = 0
        while target != None:
            length += 1
            target = target.next
        
        target = head
        if length == n:
            return head.next
        for i in range(length-n-1):
            target = target.next
        
        target.next = target.next.next
        
        return head