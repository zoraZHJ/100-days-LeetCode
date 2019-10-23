class Solution:
    def firstUniqChar(self, s: str) -> int:
        lut = {}
        for idx,char_t in enumerate(s):
            if char_t not in lut:
                lut.update({char_t: idx})
            else:
                lut.update({char_t: -1})
                
        index = -1
        for idx, value in enumerate(list(lut.values())):
            if value == -1:
                continue
            if index == -1 and value != -1:
                index = value
            else:
                index = value if value < index else index
        
        return index