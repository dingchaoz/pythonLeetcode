"""
Rules:

n pairs
( <= n
) <= (


"""

class Solution:

    # @param an integer

    # @return a list of string

   def findP(self,valuelist,solution,n,left,right):

       if len(valuelist) == 2*n:

           solution.append(valuelist)

       if left < n:

           self.findP(valuelist+'(',solution,n,left+1,right)

       if right < left:

           self.findP(valuelist+')',solution,n,left,right+1)

sl = Solution()
ans = []
sl.findP('',ans,3,0,0)
print(ans)
