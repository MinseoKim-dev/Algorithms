# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def construct_node(nums, start: int, end: int):
            if start > end:
                return None
            mid = (end+start)//2
            left = construct_node(nums, start, mid-1)
            right = construct_node(nums, mid+1, end)
            node = TreeNode(nums[mid], left, right)
            return node
        
        return construct_node(nums, 0, len(nums)-1)