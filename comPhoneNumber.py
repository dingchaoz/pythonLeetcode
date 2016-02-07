"""
1. create an array of dictionary mapping number to letters
2. letter combinations of (2,3,4) = for letter in a,b,c + letter combinations of (3,4)
3. Base case: () = ''; if len() = 0, the return letters corresponding to the number

"""

class Solution:

    def comPhoneNumer(self,s):

        map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        if len(s) == 0:

            return ''

        if s[0] not in map:

            raise LookupError("Unacceptable input.")

        if len(s) == 1:

            return map[s]

        firstletters = map[s[0]]
        restletters = self.comPhoneNumer(s[1:])

        res = []

        for letter in firstletters:

            for restletter in restletters:

                res.append(letter + restletter)

        return res

sl = Solution()
string = '23'
ans = sl.comPhoneNumer(string)
print(ans)


