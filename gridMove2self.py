"""
dp[m][n] = dp[m-1][n] + dp[m][n-1]
if m == 0 , dp[0][i] = 1, i from 0 to n - 1
if n ==0, dp[i][n] = 1, i from 0 to m -1

"""


class Solution:

    def gridmove(self,m,n):

        if m == 0 or n == 0:
            dp[m][n] = 1
            return 1

        if dp[m][n] != 0:
            return dp[m][n]

        return self.gridmove(m-1,n) + self.gridmove(m,n-1)

sl = Solution()
m,n = 3,7
dp = [[0]* n for x in range(m)]
ans = sl.gridmove(m-1,n-1)
print(ans)
