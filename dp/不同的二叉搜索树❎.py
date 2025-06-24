class Solution:
    def numTrees(self, n: int) -> int:
        '''
        三种分布
        1. 1个左节点，1个右节点
        2. 2个左节点，0个右节点
        3. 0个左节点，2个右节点
        dp[i] : 就是 元素1为头结点搜索树的数量 + 元素2为头结点搜索树的数量 +...+ 元素i为头结点搜索树的数量
        '''
        if n<=1:
            return n
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            for j in range(1,i+1):
                #当前节点作为root
                dp[i]+=dp[j-1]*dp[i-j]

        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.numTrees(19))