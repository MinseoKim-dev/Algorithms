# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        flag = 0
        first_result = None
        prev_result = None
        while l1 or l2 or flag:
            if l1 is None:
                val1 = 0
            else:
                val1 = l1.val
            if l2 is None:
                val2 = 0
            else:
                val2 = l2.val
            added = val1 + val2 + flag
            flag = 0
            if added >= 10:
                flag = 1
                added -= 10
            result = ListNode(added)
            if first_result is None:
                first_result = result
            if prev_result is not None:
                prev_result.next = result
            prev_result = result
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        return first_result
        