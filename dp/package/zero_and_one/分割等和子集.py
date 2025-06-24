from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 背包容量 sum/2 ,01 背包
        s = sum(nums)
        if s%2!=0:
            return False
        target = s //2
        dp = [0] * (target+1)
        for i in range(len(nums)):
            for j in range(target,nums[i]-1,-1):
                dp[j] = max(dp[j],dp[j-nums[i]]+nums[i])
        return dp[-1] == target


if __name__ == '__main__':
    so = Solution()
    print(so.canPartition([1,2,3,5]))