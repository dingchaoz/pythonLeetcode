"""

dp[x][y] = dp[x-1][y] + dp[x][y-1]

"""

class Solution:

    def uniquePaths(self,m,n):

        dp = [[0] * n for x in range(m)]

        for i in range(m):
            dp[i][0] = 1

        for j in range(n):
            dp[0][j] = 1

        for x in range(1,m):
            for y in range(1,n):
                dp[x][y] = dp[x-1][y] + dp[x][y-1]

        return dp[m-1][n-1]

sl = Solution()
m,n = 3,7
ans = sl.uniquePaths(m,n)
print(ans)