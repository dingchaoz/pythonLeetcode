"""
abcabc   st1
abcdabcd st2
abc      st3

res = ''
for i in range(len(st1)

    if st1[i] == st2[i] == st3[i]
        res += (st[1])

     else:

        return (res)

return(res)

"""

class Solution:

    def lcprefix(self,arrStr):

        res = ''

        for i in range(len(arrStr[0])):

            for j in range(1,len(arrStr)):

                if (i >= len(arrStr[j]) or arrStr[0][i] != arrStr[j][i]):

                    return (res)

            res += arrStr[0][i]

        return (res)

sl = Solution()
arr = ['abcabc','ab','abcdd']
ans = sl.lcprefix(arr)
print(ans)
