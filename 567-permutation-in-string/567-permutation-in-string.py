class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        window_size = len(s1)
        perm_counter = Counter(s1)
        matched = 0
        
        for i in range(len(s2)):
            if s2[i] in perm_counter:
                perm_counter[s2[i]] -= 1
                if perm_counter[s2[i]] == 0:
                    matched += 1
            
            if i >= window_size and s2[i-window_size] in perm_counter:
                if perm_counter[s2[i-window_size]] == 0:
                    matched -= 1
                perm_counter[s2[i-window_size]] += 1
            
            if matched == len(perm_counter):
                return True
        
        return False