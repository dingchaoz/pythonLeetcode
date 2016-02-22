
class Solution:

    def fnum(self,n):


        if n == 0 or n ==1:
            return 1

        return self.fnum(n-1) + self.fnum(n-2)

# f(5) = f(4) + f(3)
# f(4) = f(3) + f(2)
# f(3) = f(2) + f(1)


    def fnumDP(self,n):

        if n==0 or n==1:
            map[n] = 1
            return map[n]

        if n in map:
            return map[n]


        map[n] = self.fnumDP(n-1) + self.fnumDP(n-2)
        return map[n]


map = {}
import time

sl = Solution()
n = 50

start_time = time.time()
ans = sl.fnumDP(n)
print(ans)
print("--- %s seconds of dynamic programming ---" % (time.time() - start_time))


start_time = time.time()
ans = sl.fnum(n)
print(ans)
print("--- %s seconds of recursion---" % (time.time() - start_time))

