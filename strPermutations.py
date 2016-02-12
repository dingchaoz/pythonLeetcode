"""

cal1: allPermutations('1') = '1'
cal2:allPermutations('12') = '12','21'
cal3: allPermuations('123') = '123','132','213','231','321','312'
cal2 -cal1 = '2'+ '1','1'+'2'
cal3 - cal2 = for permutation in cal2:
                for pos in range(len(permutation)
                    diff = insert '3' at pos + permutation
"""



class Solution:

    def generatepmts(self,string,allperms):

        if len(string) == 1:
            allperms.append(string)
            return allperms

        newallperms = []
        for perm in self.generatepmts(string[:-1],allperms):
            for pos in range(len(perm)+1):
                newperm = perm[:pos] + string[-1] + perm[pos:]
                newallperms.append(newperm)

        allperms = newallperms
        return allperms

allperms = []
sl = Solution()
s = '123'
ans = sl.generatepmts(s,allperms)
print(ans)



