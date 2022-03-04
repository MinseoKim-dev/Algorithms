class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_to_here = 0
        max_sum = -999999
        
        for i in range(len(nums)):
            sum_to_here += nums[i]
            if sum_to_here < nums[i]:
                sum_to_here = nums[i]
            if max_sum < sum_to_here:
                max_sum = sum_to_here
            
        return max_sum