# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def recursive_traversal(root, output):
            
            if root is None:
                return []
            
            output.extend(recursive_traversal(root.left, []))
            output.append(root.val)
            output.extend(recursive_traversal(root.right, []))
            return output
        
        
        return recursive_traversal(root, [])