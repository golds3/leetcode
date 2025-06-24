from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy = [1]*len(ratings)
        for i in range(len(ratings)-1):
            if ratings[i+1] > ratings[i] and candy[i+1]<=candy[i]:
                candy[i+1] = candy[i]+1
        for i in range(len(ratings)-1,0,-1):
            if ratings[i-1] > ratings[i] and candy[i-1]<=candy[i]:
                candy[i-1] = candy[i]+1
        return sum(candy)

if __name__ == '__main__':
    s = Solution()
    print(s.candy([1,2,87,87,87,2,1]))