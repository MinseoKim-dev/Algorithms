# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        node = head
        while node.next:
            node = node.next
            count += 1
        
        middle = (count + 1) // 2
        node = head
        for i in range(middle):
            node = node.next
        return node
            