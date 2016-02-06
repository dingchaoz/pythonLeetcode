"""
1. sort the array in asc
2. two pointers, i from the 0 index, j from the last index
3. compare the sum of the the numbers at the index
4. if the sum < target, increase the index i by 1
   else reduce the index j by 1
"""

class Solution:


    def twoSum(self,array,target):

        array.sort()

        i,j = 0, len(array) - 1

        res = []


        while j > i:

            temp = array[i] + array[j]

            if temp == target:

                tup = (array[i],array[j])

                res.append(tup)

                i += 1

            elif temp >= target:

                j -= 1
            else:
                i += 1

        print(res)

        return (1)


a = [3, 4, 5,10, 9,8,7, 1,5]

t = 8
solution = Solution()
solution.twoSum(a,t)

