class Solution:
    def countAndSay(self, n: int) -> str:
        if(n==1):
            return '1'
        str_pre = self.countAndSay(n-1)
        len_pre = len(str_pre)

        print_str = ""
        cur_num = str_pre[0]
        i = 1
        count_num = 1
        while(i<len_pre):
            if(str_pre[i] == cur_num):
                count_num += 1
            else:
                print_str = print_str + str(count_num) + cur_num
                cur_num = str_pre[i]
                count_num = 1
            i+=1
        print_str = print_str + str(count_num) + cur_num
        return print_str
            