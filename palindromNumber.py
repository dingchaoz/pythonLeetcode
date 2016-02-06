"""

45654
1st digit = 45654/10000
last digit = 45654%10
new numbers stripping out 1st and last = 45654%10000/10
continue the 1st and last digit compare


"""

class Solution:

    def pnum(self,num):

        base = 1

        while num/base >= 10:

            base *= 10

        while num > 0:

            if num/base != num%10:

                return -1

            num = num%base/10
            base = base/100

        return 1

sl = Solution()
num = -55
ans = sl.pnum(num)
print(ans)
