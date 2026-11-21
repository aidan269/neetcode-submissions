class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s_t = {}
        mapping_t_s = {}

        for ch1, ch2 in zip(s,t):
            if ch1 in mapping_s_t and mapping_s_t[ch1] != ch2:
                return False
            if ch2 in mapping_t_s and mapping_t_s[ch2] != ch1:
                return False 
            else: 
                mapping_s_t[ch1] = ch2 
                mapping_t_s[ch2] = ch1
        return True 

