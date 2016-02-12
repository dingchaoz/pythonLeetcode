"""
strcom('1') = 1
strcom('12') = 1,2,12
strcom('123') = 1,2,3,12,13,23,123
strcom('123') - strcom('12') = '3','13','23','123' = for x in strcom('12') + '3', '3'
allCombinations = [] array of strings to hold results
"""
allcoms = []

class Solution:

    def strcom(self,string):

        if len(string) == 0 or len(string) == 1:
            allcoms.append(string)
            return allcoms

        newcoms = [string[-1]]
        for com in self.strcom(string[:-1]):
            newcom = com
            newcom += string[-1]
            newcoms.append(newcom)
        allcoms.extend(newcoms)
        return allcoms


sl = Solution()
string = '123'
ans = sl.strcom(string)
print(ans)

