"""
This script solves to reach position(i,j) with k turns
the count paths cpt equal to the sum of along the row and the column
cpt(i,j,k) = cpt(i-1,j,k,0) + cpt(i,j-1,k,1)

cpt(i,j,k,0) = cpt(i-1,j,k,0) + cpt(i,j-1,k-1,1)
cpt(i,j,k,1) = cpt(i,j-1,k,1) + cpt(i-1,j,sk-1,0)

"""



class Solution:

    def cptd(self,m,n,k,d):

        if m == 0 and n == 0:
            return 1

        if m <0 or n <0:
            return 0

        if k==0:
            if d == 0 and n ==0:
                return 1
            if d == 1 and m ==0:
                return 1

            return 0

        if d == 0:
            return self.cptd(m,n-1,k,0) + self.cptd(m-1,n,k-1,1)

        if d == 1:
            return self.cptd(m-1,n,k,1) + self.cptd(m,n-1,k-1,0)



sl = Solution()
m,n,k = 3,3,2
ans1 = sl.cptd(m-1,n,k,1)
ans2 = sl.cptd(m,n-1,k,0)
print(ans1+ans2)

