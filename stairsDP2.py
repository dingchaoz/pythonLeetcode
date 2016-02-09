map = {}

class Solution:

    def stairs(self,n):

        if n < 0:
            return 0

        if n == 0:
            return 1

        if n in map:
            return map[n]
        else:
            map[n] = self.stairs(n-1) + self.stairs(n-2) + self.stairs(n-3)
            return map[n]

sl = Solution()
n = 4
ans = sl.stairs(n)
print(ans)