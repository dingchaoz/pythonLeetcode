"""
dp[m][n] = dp[m-1][n] + dp[m][n-1]
if m == 0 , dp[0][i] = 1, i from 0 to n - 1
if n ==0, dp[i][n] = 1, i from 0 to m -1

"""

class Solution:

    def gridmove(self,m,n):

        #dp = [[0] * n for x in range(m)]

        if dp[m-1][n-1] != 0:
            return dp[m-1][n-1]

        for i in range(m):
            dp[i][0] = 1

        for j in range(n):
            dp[0][j] = 1


        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = self.gridmove(i,j+1) + self.gridmove(i+1,j)
                #dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]

m,n = 3,7
dp = [[0] * n for x in range(m)]
sl = Solution()
ans = sl.gridmove(m,n)
print(ans)