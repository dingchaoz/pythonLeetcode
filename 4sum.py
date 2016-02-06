class Solution:

    def foursum(self,array,target):

        array.sort()

        res = []

        i = 0

        for i in range(len(array) - 3):

            for j in range(i+1,len(array)-2):

                z = j +1
                w = len(array) - 1
                diff = target - array[j] - array[i]
                while w > z:

                    temp = array[z] + array[w]

                    if temp == diff:

                        tup = (array[i],array[j],array[z],array[w])
                        res.append(tup)
                        z += 1
                    elif temp > diff:
                        w -= 1
                    else:
                        z +=1

        return(res)

nums = [1,2,3,4,5,6,7,8]
t = 14
solution = Solution()
ans = solution.foursum(nums,t)
print(ans)
