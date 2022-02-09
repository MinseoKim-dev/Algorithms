class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        threshold = math.floor(len(nums)/2) + 1
        distinct_numbers = set(nums)
        for number in distinct_numbers:
            count = 0
            for num in nums:
                if (num == number):
                    count += 1
                if (count == threshold):
                    return number