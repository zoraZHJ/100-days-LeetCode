class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cmnPre = ""
        if len(strs) == 0:
            return cmnPre
        
        done = False
        for l_idx, l in enumerate(strs[0]):
            if not done:   #if break, the process of finding common prefix ended.
                for idx,str in enumerate(strs):
                    if len(str)<=l_idx:
                        done = True
                        break
                    elif len(str)>l_idx and str[l_idx] != l:
                        done = True
                        break
                    if idx == (len(strs) - 1):
                        cmnPre = cmnPre + l

        return cmnPre
