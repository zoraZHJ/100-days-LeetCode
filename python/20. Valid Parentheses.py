class Solution:
    def isValid(self, s: str) -> bool:
        len_s = len(s)
        if len_s == 0:
            return True
        elif len_s == 1:
            return False
        stack = []
        for i in range(len_s):
            if s[i] in ['(', '[', '{']:
                stack.append(s[i])
            elif len(stack) != 0:
                if (s[i] == ')' and stack[-1]=='(') or (s[i] == ']' and stack[-1]=='[') or (s[i] == '}' and stack[-1]=='{'):
                    stack = stack[:-1]
                else:
                    return False
            else:
                return False

        if len(stack) == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    s = "()"
    s = '()[]{}'
    s = '(]'
    s = '([)]'
    s = '{[]}'
    s = '}{}'
    sln = Solution()
    res = sln.isValid(s)
    print(res)