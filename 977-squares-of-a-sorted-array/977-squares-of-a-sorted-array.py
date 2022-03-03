class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        negative = []
        positive = []
        count = len(nums)
        result = []
        for number in nums:
            if number >= 0:
                positive.append(number**2)
            else:
                negative.append(number**2)
        
        negative = negative[::-1]
        
        i, j = 0, 0
        while count > 0 and i < len(positive) and j < len(negative):
            if positive[i] >= negative[j]:
                result.append(negative[j])
                j += 1
            else:
                result.append(positive[i])
                i += 1
            count -= 1
        
        if count != 0:
            if i == len(positive):
                result.extend(negative[j:])
            elif j == len(negative):
                result.extend(positive[i:])
        
        return result
            
        