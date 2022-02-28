# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        pre = head
        target = head.next
        while target is not None:
            if target.val == pre.val:
                #deleting node
                pre.next = target.next
            else:
                pre = target
            target = target.next
        return head
                
        