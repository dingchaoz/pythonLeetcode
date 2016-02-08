"""
number of paths to(m,n,k)
p(m.n,k) = p(m-1,n,k-n(m,n)) + p(m,n-1,k-n(m,n))

"""

class Solution:

    def numpaths(self,matrix,m,n,k):

        if m < 0 or n <0 :

            return 0

        if m == 0 and n == 0:

            return k == matrix[m][n]

        return self.numpaths(matrix,m-1,n,k-matrix[m][n]) + self.numpaths(matrix,m,n-1,k-matrix[m][n])


matrix = [[1,2,3],[4,6,5],[3,2,1]]

sl = Solution()
ans = sl.numpaths(matrix,2,2,12)
print(ans)


