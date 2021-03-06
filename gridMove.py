"""

dp[x][y] = dp[x-1][y] + dp[x][y-1]

"""

class Solution:

    def gridmove(self,m,n):

        dp = [[0] * n for x in range(m)]

        for i in range(m):
            dp[i][0] = 1

        for j in range(n):
            dp[0][j] = 1

        if dp[m-1][n-1] != 0:
            return dp[m-1][n-1]

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = self.gridmove(i,j+1) + self.gridmove(i+1,j)
                #dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]


sl = Solution()
ans = sl.gridmove(3,7)
print(ans)