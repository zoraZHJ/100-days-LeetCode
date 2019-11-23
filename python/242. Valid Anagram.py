class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = {}
        for s_t in s:
            if s_t not in hash:
                hash.update({s_t: 1})
            else:
                hash[s_t] += 1
        
        for t_t in t:
            if t_t in hash:
                if hash[t_t] > 0:
                    hash[t_t] -= 1
                else:
                    return False
            else:
                return False
        for val in hash.values():
            if val > 0:
                return False
        return True