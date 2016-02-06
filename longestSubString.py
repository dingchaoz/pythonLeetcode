"""
1. cur_string; max_len; cur_len; visisted_chars
2. For i in string:
    if i not in visited_chars:
       cur_string.append(i)
       cur_len += 1
    elseif i in visited_chars:
       if i in cur_string:
         max_len = max(max_len,cur_len)
         cur_len = 0
         cur_string = []
       else if i not in cur_string:
         cur_string.append(i)
         cur_len += 1

    return(max_len)
"""

class Solution:

    def lstr(self,string):

        cur_str = [string[0]]
        cur_len = 1
        max_len = 1
        vis_chars = [string[0]]

        for i in range(1,len(string)):

            s = string[i]

            if s in vis_chars:

                if s in cur_str:

                    max_len = max(max_len,cur_len)
                    cur_len = 1
                    cur_str = [string[i]]

                else:

                    cur_str.append(s)
                    cur_len += 1

            else:

                cur_str.append(s)
                vis_chars.append(s)
                cur_len +=1
                max_len = max(max_len,cur_len)

        return (max_len)

solution = Solution()

s = 'GEEKSFORGEEKS'
ans = solution.lstr(s)
print(ans)




