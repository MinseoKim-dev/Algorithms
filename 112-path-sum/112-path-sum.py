# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        
        if not root:
            return False
        """
        if targetSum < 0:
            return False
        """
        
        leftover = targetSum - root.val
        
        if not leftover and not root.left and not root.right:
            return True
        
        if self.hasPathSum(root.left, leftover) or self.hasPathSum(root.right, leftover):
            return True
        
        