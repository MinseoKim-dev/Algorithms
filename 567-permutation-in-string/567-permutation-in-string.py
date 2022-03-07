class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        window_size = len(s1)
        perm_counter = Counter(s1)
        
        for i in range(len(s2)):
            if s2[i] in perm_counter:
                perm_counter[s2[i]] -= 1
            
            if i >= window_size and s2[i-window_size] in perm_counter:
                perm_counter[s2[i-window_size]] += 1
            
            if all([perm_counter[l]==0 for l in perm_counter]):
                return True
        
        return False