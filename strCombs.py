__author__ = 'ks692'

map = {}
class Solution:

	def strcombs(self,n,string,map):

		if len(string) == 0:
			map[0] = ''
			return list(map.values())

		if len(string) == 1:
			map[1] = string
			return list(map.values())

		if n in map:
			return list(map.values())

		newsubs = []
		for sub in self.strcombs(n-1,string[:-1],map):
			newsub = sub
			newsub += string[-1]
			newsubs.append(newsub)

		newsubs.append(string[-1])
		map[n] = newsubs

		result = []
		extend = result.extend
		for l in list(map.values()):
			extend(l)

		return result



st = '123'
n = len(st)
sl = Solution()
ans = sl.strcombs(n,st,map)
print(ans)
