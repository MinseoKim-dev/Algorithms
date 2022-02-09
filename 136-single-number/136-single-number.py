class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        cand = []
        for number in nums:
            if number in cand:
                cand.remove(number)
            else:
                cand.append(number)
                
        return cand[0]