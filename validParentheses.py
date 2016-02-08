"""
1. creat a map, key is right parenthsis, value is left parenthsis
2. create a stack reading the strings and add to the stack when there is a left parenthsis
3. if right parenthsis, compare if the last element of stack is equal to the value to the key
   if yes, pop up the last element of stack, else, return false
4. return true if stack is empty


"""



class Solution:

    def isValid(self,s):

        map = {")": "(", "]": "[", "}": "{"}

        stack = []

        for i in range(len(s)):

            if s[i] in map.values():

                stack.append(s[i])

            elif len(stack) == 0 or map[s[i]] != stack.pop():

                return False

            else:

                continue


        return len(stack) == 0

sl = Solution()
string = '{'
ans = sl.isValid(string)
print(ans)

