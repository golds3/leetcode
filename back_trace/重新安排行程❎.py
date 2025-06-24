from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        hash = defaultdict(list)
        for v in tickets:
            hash[v[0]].append(v[1])
        for _,v in hash.items():
            v.sort(reverse=True) # 逆序排序，方便后面先取最后一个
        res = []
        def dfs(start:str):
            while hash[start]:
               next =  hash[start].pop()
               dfs(next)
            res.append(start)
        dfs('JFK')
        return res[::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","JFK"],["ATL","AAA"],["AAA","ATL"],["ATL","BBB"],["BBB","ATL"],["ATL","CCC"],["CCC","ATL"],["ATL","DDD"],["DDD","ATL"],["ATL","EEE"],["EEE","ATL"],["ATL","FFF"],["FFF","ATL"],["ATL","GGG"],["GGG","ATL"],["ATL","HHH"],["HHH","ATL"],["ATL","III"],["III","ATL"],["ATL","JJJ"],["JJJ","ATL"],["ATL","KKK"],["KKK","ATL"],["ATL","LLL"],["LLL","ATL"],["ATL","MMM"],["MMM","ATL"],["ATL","NNN"],["NNN","ATL"]]))