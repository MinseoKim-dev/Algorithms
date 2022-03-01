class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        going_high = 1
        
        while start <= end:
            mid = (start+end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid-1
                going_high = 0
            else:
                start = mid+1
                going_high = 1
                
        return mid+going_high