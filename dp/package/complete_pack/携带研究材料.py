from typing import List


class Solution:
    def fn(self,things:List[int],value:List[int],size:int)->int:
        dp = [0]*(size+1)

        for k,v in enumerate(things):
            for j in range(v,size+1):
                dp[j] = max(dp[j],dp[j-v]+value[k])
        return dp[-1]


if __name__ == '__main__':
    n,v = map(int,input().split())
    things = [0]*(n)
    value = [0]*n
    for i in range(n):
        things[i],value[i] = map(int,input().split())
    print(Solution().fn(things,value,v))