class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        c1 = Counter(nums1)
        c2 = Counter(nums2)
        result = []
        
        for i in c1:
            if i in c2:
                appearance = min(c1[i], c2[i])
                for j in range(appearance):
                    result.append(i)
        
        return result