"""
f(n) = n-1 * (f(n-1) + f(n-2))

"""

class Solution:

    def cd(self,n):

        if n == 1:

            return 0

        if n == 2:

            return 1

        return (n-1)*(self.cd(n-1) + self.cd(n-2))

sl = Solution()
n = 2
ans = sl.cd(n)
print(ans)