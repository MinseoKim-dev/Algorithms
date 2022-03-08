"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if root is None:
            return None
        
        node_to_visit = [root]
        while node_to_visit:
            next_level = []
            for i in range(len(node_to_visit)):
                if i+1 < len(node_to_visit):
                    node_to_visit[i].next = node_to_visit[i+1]
                else:
                    node_to_visit[i].next = None
                if node_to_visit[i].left:
                    next_level.append(node_to_visit[i].left)
                    next_level.append(node_to_visit[i].right)
            node_to_visit[:] = []
            node_to_visit.extend(next_level[:])
            
        return root    
        
            