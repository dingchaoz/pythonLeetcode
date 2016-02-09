"""
paths to the nth step p(n) = p(n-1) + p(n-2) + p(n-3)
base case:
n < 0, p(n) = 0
n == 0, p(n) = 1
map = []
return map[n]


"""

class Solution:

    def stairs(self,n,map):

        if n < 0:
            map[n] = 0
            return map[n]

        if n == 0:
            map[n] = 1
            return map[n]


        if map[n]:
            return map[n]

        else:
            map[n] = self.stairs(n-1,map) + self.stairs(n-2,map) + self.stairs(n-3,map)
            return map[n]

sl = Solution()
n = 4
map = [None] * (n+1)
ans = sl.stairs(n,map)
print(ans)


