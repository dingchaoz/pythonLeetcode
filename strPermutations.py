"""

cal1: allPermutations('1') = '1'
cal2:allPermutations('12') = '12','21'
cal3: allPermuations('123') = '123','132','213','231','321','312'
cal2 -cal1 = '2'+ '1','1'+'2'
cal3 - cal2 = for permutation in cal2:
                for pos in range(len(permutation)
                    diff = insert '3' at pos + permutation
"""
# map = {}
class Solution:
#
#     def allpermts(self,string,map):
#
#         if len(string) == 1:
#             map[1] = string
#             return map[1]
#
#         if len(string) in map:
#             return list(map.values())
#
#         newpemts = []
#         for pemts in self.allpermts(string[:-1],map):
#             for pos in range(len(pemts)):
#                 newpemt = pemts[:pos] + string[-1] + pemts[pos:]
#                 newpemts.append(newpemt)
#
#         map[len(string)] = newpemts
#
#         return list(map.values())


    def perm(self,s):
        res = []
        if len(s) == 1:
            res = [s]
            return [s]

        if s in cache:
            return cache[s]

        else:
            for i, c in enumerate(s):
                for p in self.perm(s[:i] + s[i+1:]):
                    res += 1
        cache[s] = res
        return res




# allpmts = []
#
# class Solution:
#
#     def strpmt(self,string):
#
#         if len(string) == 0:
#             allpmts.extend('')
#             return allpmts
#
#         if len(string) == 1:
#             allpmts.append(string)
#             return allpmts
#
#         newpmts = []
#         for pmt in self.strpmt(string[:-1]):
#             for pos in range(len(pmt)):
#                 newpmt = pmt[:pos] + string[-1] + pmt[pos:]
#                 newpmts.append(newpmt)
#
#         allpmts = newpmts
#         return allpmts
cache = {}
sl = Solution()
s = '123'
ans = sl.perm(s)
print(ans)



