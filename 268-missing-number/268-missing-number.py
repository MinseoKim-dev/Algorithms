class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        last = len(nums)
        entire_sum = int(last*(last+1)/2)
        for number in nums:
            entire_sum -= number
        return entire_sum