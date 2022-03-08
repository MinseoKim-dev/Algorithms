# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    
        
        def recursive_dfs(node1, node2):
            if node1 and node2:
                left = recursive_dfs(node1.left, node2.left)
                right = recursive_dfs(node1.right, node2.right)
                return TreeNode(node1.val + node2.val, left, right)
            elif node1:
                return node1
            elif node2:
                return node2
            else:
                return None
        
        return recursive_dfs(root1, root2)
            