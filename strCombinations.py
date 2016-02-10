"""
strcom('1') = 1
strcom('12') = 1,2,12
strcom('123') = 1,2,3,12,13,23,123
strcom('123') - strcom('12') = '3','13','23','123' = for x in strcom('12') + '3', '3'
allCombinations = [] array of strings to hold results
"""

allCombinations = []

class Solution:

    def strcom(self,string):

        length = len(string)

        if length == 0:
            allCombinations.append('')
            return allCombinations

        if length == 1:
            allCombinations.append(string)
            return allCombinations

        newsubstrings = [string[-1]]
        for substring in self.strcom(string[:-1]):
            newsubstring = substring
            newsubstring += string[length-1]
            newsubstrings.append(newsubstring)

        allCombinations.extend(newsubstrings)
        return allCombinations

sl = Solution()
string = '123'
ans = sl.strcom(string)
print(ans)