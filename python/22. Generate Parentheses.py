class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(res, tmp, n, left, right):
            if right == n:
                res.append(tmp)
            if left < n:
                dfs(res, tmp + "(", n, left+1, right)
            if left > right:
                dfs(res, tmp + ")", n, left, right+1)
        
        dfs(res, "", n, 0, 0)

        return res