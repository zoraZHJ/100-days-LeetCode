class Solution:
    def romanToInt(self, s: str) -> int:
        str_len = len(s)
        idx = 0
        roman2Int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        while(idx < str_len):
            if s[idx] in roman2Int:
                if ((idx+1) < str_len) and (s[idx+1] in roman2Int) and (roman2Int[s[idx]] < roman2Int[s[idx+1]]):
                        val_t = roman2Int[s[idx+1]] - roman2Int[s[idx]]
                        idx += 2
                else:
                    val_t = roman2Int[s[idx]]
                    idx += 1
                res += val_t
        return res