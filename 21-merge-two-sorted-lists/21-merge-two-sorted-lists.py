# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if l1 and l2:
            if l1.val > l2.val:
                head = ListNode(l2.val)
                l2 = l2.next
            else:
                head = ListNode(l1.val)
                l1 = l1.next
        elif l1:
            head = ListNode(l1.val)
            l1 = l1.next
        elif l2:
            head = ListNode(l2.val)
            l2 = l2.next
        else:
            return None
            
        ans = head
        
        while l1 or l2:
            if l1 and l2:
                if l1.val > l2.val:
                    ans.next = l2
                    ans = ans.next
                    l2 = l2.next
                else:
                    ans.next = l1
                    ans = ans.next
                    l1 = l1.next
            elif l1:
                ans.next = l1
                ans = ans.next
                l1 = l1.next
            elif l2:
                ans.next = l2
                ans = ans.next
                l2 = l2.next
                
        
        return head
                
                    
            