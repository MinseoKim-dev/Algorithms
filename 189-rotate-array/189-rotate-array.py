class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        modded_k = k % len(nums)
        
        nums_shallow_copied = nums[:]
        
        for i in range(len(nums)):
            nums[(i + modded_k) % len(nums)] = nums_shallow_copied[i]