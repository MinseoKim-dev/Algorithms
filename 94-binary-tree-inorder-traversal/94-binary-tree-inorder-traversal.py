# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def recursive_traversal(root):
            
            if root is None:
                return []

            return recursive_traversal(root.left) + [root.val] + recursive_traversal(root.right)
        
        
        return recursive_traversal(root)