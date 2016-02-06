"""
abbccbbbad
l(1,10) =
   if the 1st char == 10th char:

        l(1,10) == 2 + l(2,9)
   else:

        l(1,10) == max(l(1,9),l(2,10))

l(0) = 0
l(1,1) = 1
l(1,2) = 1 if 1st char != 2nd char
         2 if 1st char == 2nd char
"""

class Solution:

    def lps(self,string,m,n):

        res = 0

        if n == m:
            res = 1
            return res

        if n == m +1 and string[m] == string[n]:
            res = 2
            return res


        if string[m] == string[n]:
            # if self.lps(string,m+1,n-1) == 1 and n == m +2:
            #     res = 2 + self.lps(string,m+1,n-1)
            #     return res
            if self.lps(string,m+1,n-1) == n-m-1:
                res = 2 + self.lps(string,m+1,n-1)
                return res
            else:
                res = self.lps(string,m+1,n-1)
                return res
        else:
            res = max(self.lps(string,m,n-1),self.lps(string,m+1,n))
            return res

s = 'abxbca'
n = len(s) - 1
sl = Solution()
ans = sl.lps(s,0,n)
print(ans)

