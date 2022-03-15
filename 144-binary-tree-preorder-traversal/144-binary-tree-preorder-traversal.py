# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []
        
        result = []
        def recursive_preorder(node):
            if node is None:
                return
            result.append(node.val)
            recursive_preorder(node.left)
            recursive_preorder(node.right)
            
        recursive_preorder(root)
        return result