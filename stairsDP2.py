# Using dynamic programmming to solve stairs problems

class Solution:

    def stairs(self,n):

        if n < 0:
            return 0

        if n == 0 or n ==1:
            return 1

        if n in map:
            return map[n]
        else:
            map[n] = self.stairs(n-1) + self.stairs(n-2) + self.stairs(n-3)
            #map[n] = map[n-1] + map[n-2] + map[n-3]
            return map[n]

map = {} # A dictionary, n is the key and map[n] is the value
sl = Solution()
n = 4
ans = sl.stairs(n)
print(ans)