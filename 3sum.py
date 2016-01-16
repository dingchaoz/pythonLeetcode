"""

Given an array S of n integers, are there elements a,b,c in S such that a+b+c = 0?
Find all unique triplets in the array which gives sum of zero

Note:
Elements in a triplet(a,b,c) must be in non-descending order(ie,a<=b<=c)
The solution set must not contain duplicate triplets,
    For example, given array S = [-1, 0, 1, 2, -1, -4]

    A solution set is:
        (-1,0,1)
        (-1,-1,2)


"""
# maybe try to solve a 2sum problem first
class Solution:

    def threeSum(self,nums):
        """
        :rtype: object
        :param nums: List[int]
        :return:  List[List[int]]
        """
        nums.sort()
        res = []

        for start in range(len(nums)):

            end = len(nums) - start

            for i in range(1,end):

                twosum = nums[start] + nums[end]

                if twosum + nums[i] == 0:

                    res = [nums[start],nums[i],nums[end]]

                elif twosum + nums[i]


            return res

# create an object named solution of Class Solution
solution = Solution()

# call Class Solution's defined method threeSum and return into ans variable
ans = solution.threeSum([-1, 0, 1, 2, -1, -4])

print(ans)





