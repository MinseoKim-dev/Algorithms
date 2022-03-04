class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) > 1:
        
            left, right = 0, 0
        
            while right < len(nums):
                if nums[right] != 0:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                right += 1
        
            