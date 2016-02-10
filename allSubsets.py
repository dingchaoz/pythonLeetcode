"""
[1] : [1], []
[1,2]: [1,2],[1],[2],[]
allsubsets[1,2] - [1] = [1,2],[2]
assets(list,n) = assets(list,n-1) + [for x in assets(list,n-1) x.append.list[n]]
need an array of array to hold all intermediate results

"""

all_subsets = [[]]

class Solution:

    def assets(self,list,n):

        if n == 0:
            temp = [list[n]]
            all_subsets.append(temp)
            return all_subsets

        else:
            new_subsets = []
            for subset in self.assets(list,n-1):
                new_subset = []
                new_subset.extend(subset)
                new_subset.append(list[n])
                new_subsets.append(new_subset)
            all_subsets.extend(new_subsets)


        return all_subsets

sl = Solution()
list = [1,2,3,4]
n = len(list) - 1
ans = sl.assets(list,3)
print(ans)

