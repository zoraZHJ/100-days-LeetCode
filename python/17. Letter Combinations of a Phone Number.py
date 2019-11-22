class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d2c_dict = {"2": "abc", "3": "def", "4": "ghi",
        "5": "jkl", "6": "mno", "7": "pqrs",
        "8": "tuv", "9": "wxyz"}

        tmp = []
        res = []
        for d in digits:
            if tmp == []:
                for v in d2c_dict[d]:
                    res.append(v)
            else:
                for tmp_s in tmp:
                    for v in d2c_dict[d]:
                        tmp_s_add = tmp_s + v
                        res.append(tmp_s_add)
            tmp = res
            res = []
        
        res = tmp
        return res
