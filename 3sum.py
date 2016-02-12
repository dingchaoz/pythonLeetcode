"""

Given an array S of n integers, are there elements a,b,c in S such that a+b+c = 0?
Find all unique triplets in the array which gives sum of zero

Note:
Elements in a triplet(a,b,c) must be in non-descending order(ie,a<=b<=c)
The solution set must not contain duplicate triplets,
    For example, given array S = [-1, 0, 1, 2, -1, -4];s

    A solution set is:
        (-1,0,1)
        (-1,-1,2)

1. sort the array
2. 3 pointers, i,j,z
3. diff = target - array[i], we use 2sum approach to find j,z sum up equal to diff
4. If the sum of j,z > diff, z+=1 , otherwise j -=1

"""
# solved 2sum,3sum,4sum problems
class Solution:

    def threeSum(self,array,target):
        """
        :rtype: object
        :param nums: List[int]
        :return:  List[List[int]]
        """
        array.sort()
        res = []

        for i in range(len(array) - 2):

            j = i + 1
            z = len(array) - 1

            diff = target - array[i]

            while z > j:

                temp = array[j] + array[z]

                if temp == diff:

                    tup = (array[i],array[j],array[z])
                    res.append(tup)

                    j += 1

                elif temp > diff:

                    z -= 1

                else:
                    j += 1


        return res






# create an object named solution of Class Solution
solution = Solution()

# call Class Solution's defined method threeSum and return into ans variable
ans = solution.threeSum([5, 3, 0, 2, 1, 6],8)

print(ans)





