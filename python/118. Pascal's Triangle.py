class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        list_res = []
        list_tmp = []
        if numRows == 0:
            list_res.append(list_tmp)
            return list_res
        list_tmp = [1]
        list_res.append(list_tmp)
        if numRows == 1:
            return list_res

        list_pre = list_tmp
        for row in range(2, numRows + 1):
            len_pre = len(list_pre)
            list_tmp = [1]
            for idx in range(len_pre-1):
                num = list_pre[idx] + list_pre[idx+1]
                list_tmp.append(num)
            list_tmp.append(1)
            list_res.append(list_tmp)
            list_pre = list_tmp
        return list_res