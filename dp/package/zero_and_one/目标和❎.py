from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if abs(target)>s:
            return 0
        if (s+target) % 2 !=0:
            return 0
        # 可以分成两部分 left(全部为+)，right(全部为-)
        left = (s+target)//2 # 也就是背包容量
        dp = [0]*(left+1)
        dp[0] = 1
        for n in nums:
            for j in range(left, n-1, -1):
                dp[j] += dp[j-n]
        return dp[-1]


if __name__ == '__main__':
    so = Solution()
    print(so.findTargetSumWays([1,1,1,1,1],3))