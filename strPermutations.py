"""

cal1: allPermutations('1') = '1'
cal2:allPermutations('12') = '12','21'
cal3: allPermuations('123') = '123','132','213','231','321','312'
cal2 -cal1 = '2'+ '1','1'+'2'
cal3 - cal2 = for permutation in cal2:
                for pos in range(len(permutation)
                    diff = insert '3' at pos + permutation
"""
allpmts = []

class Solution:

    def strpmt(self,string):

        if len(string) == 0:
            allpmts.extend('')
            return allpmts

        if len(string) == 1:
            allpmts.append(string)
            return allpmts

        newpmts = []
        for pmt in self.strpmt(string[:-1]):
            for pos in range(len(pmt)):
                newpmt = pmt[:pos] + string[-1] + pmt[pos:]
                newpmts.append(newpmt)

        allpmts = newpmts
        return allpmts

sl = Solution()
s = '1'
ans = sl.strpmt(s)
print(ans)



