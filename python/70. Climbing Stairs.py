class Solution:
    def climbStairs(self, n: int) -> int:
        P = []
        if(n==0):
            return 0
        elif(n==1):
            return 1
        elif(n==2):
            return 2
        P = [0, 1, 2]
        for i in range(3, n+1):
            P.append(P[i-1] + P[i-2])
        return P[n]