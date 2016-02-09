"""
if the middle index  == its value, return middle index
if middle index < its value , search the left half
if middle index > its value, search the right half

"""

class Solution():

    def mindex(self,list,start,end):

        if end == 0 or start == len(list):
            return None

        middle_index = (start+end) / 2
        middle_value = list[middle_index]

        if middle_value == middle_index:
            return middle_index
        elif middle_value < middle_index:
            return self.mindex(list,middle_index+1,end)
        else:
            return self.mindex(list,start,middle_index - 1)



sl = Solution()
list = [-40,-10,1,3,5,7,8,9,10,10]
end = len(list) - 1
start = 0
ans = sl.mindex(list,start,end)
print(ans)