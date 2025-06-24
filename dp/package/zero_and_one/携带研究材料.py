from typing import List


class Solution:
    """
    https://kamacoder.com/problempage.php?pid=1046
    """
    def fn(self,things:List[int],values:List[int],weight:int)->int:
        dp = [[0 for _ in range(weight+1)] for _ in range(len(things))]
        for i in range(things[0],weight+1):
            dp[0][i] = values[0]
        for i in range(1,len(things)):
            for j in range(1,weight+1):
                if j<things[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i-1][j-things[i]]+values[i])
        return dp[-1][-1]

    # 一维dp优化
    """
    一定要按照先物品后背包的顺序遍历
    如果物品只能用一次（零一背包），那么需要倒序遍历
    物品可以用多次---正序遍历
    """
    def fn2(self,things:List[int],values:List[int],weight:int)->int:
        dp = [0 for _ in range(weight+1)]
        for i in range(len(things)):
            for j in range(weight,things[i]-1,-1):
                    dp[j] = max(dp[j],dp[j-things[i]]+values[i])
        return dp[-1]


if __name__ == '__main__':
    inp = input().split(" ")
    _,n = int(inp[0]),int(inp[1])
    things = [int(v) for v in input().split(" ")]
    weight = [int(v) for v in input().split(" ")]
    s = Solution()
    print(s.fn2(things,weight,n))
