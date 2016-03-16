#write a function will return a median of two sorted arrays
# assume arrays only have positive integers, sorted from smaller to bigger numbers
# assume lenghts of arrays could be different and big.
# A=[1,3,5]
# B=[2,4]
# findMedian(A,B) -->3

"""
find the kth smallest element in array A,B
for k = 4, look at the 2nd elemnent of A and B
because a1 < a2 < a3, so if
a2 <= b2, then the 4th smallest element will be in the 2nd half of
array B


find out the median element
median element is the
len(a) + len(b) / 2 if the combined length is odd number
len(a) + len(b) /2 or len(a) + len(b) /2 + 1 if the combined length is even number


"""


class Solution:

    def getKthElement(self,A,B,k):

        lenA, lenB = len(A),len(B);

        if lenA > lenB:
            return self.getKthElement(B,A,k)

        if len(A) == 0:
            return B[k-1]

        if k == 1:
            return min(A[0],B[0])

        pa = min(k/2, lenA)
        pb = k - pa

        if A[pa - 1] <= B[pb-1]:
            return self.getKthElement(A[pa:],B,pb)

        else:
            return self.getKthElement(A,B[pb:],pa)




    def getMedian(self,A,B):
        lenA, lenB = len(A),len(B)

        if (lenA+lenB) % 2 == 1:
            return self.getKthElement(A,B,(lenA+lenB)/ 2 + 1)
        else:
            return (self.getKthElement(A,B,(lenA+lenB)/2))/2.0 + self.getKthElement(A,B,(lenA+lenB)/2 + 1)/2.0


A=[]
B=[2,4,6]

solution = Solution()
ans = solution.getMedian(A,B)
print ans