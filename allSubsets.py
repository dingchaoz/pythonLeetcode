"""
[1] : [1], []
[1,2]: [1,2],[1],[2],[]
allsubsets[1,2] - [1] = [1,2],[2]
assets(list,n) = assets(list,n-1) + [for x in assets(list,n-1) x.append.list[n]]
need an array of array to hold all intermediate results

"""
# map = {}
# class Solution:
#     def assets(self,l,n,map):
#         if len(l) == 1:
#             map[1] = [l[0]]
#             return map[n]
#         if n in map:
#             return map[n]
#         allnewsubs = []
#
#         for subs in self.assets(l[:-1],n-1,map):
#             newsubs = []
#             newsubs.extend([subs])
#             newsubs.extend([l[-1]])
#             allnewsubs.append(newsubs)
#         map[n] = allnewsubs
#         map[n].append([l[-1]])
#
#         result = []
#         extend = result.extend
#
#         for l in list(map.values()):
#             extend(l)
#
#         return result
all_subsets = [[]]

class Solution:

    def assets(self,l):

        if len(l) == 1:
            temp = [l[-1]]
            all_subsets.append(temp)
            return all_subsets

        else:
            new_subsets = []
            for subset in self.assets(l[:-1]):
                new_subset = []
                new_subset.extend(subset)
                new_subset.append(l[-1])
                new_subsets.append(new_subset)
            all_subsets.extend(new_subsets)


        return all_subsets

sl = Solution()
l = [1,2,3]
ans = sl.assets(l)
print(ans)

