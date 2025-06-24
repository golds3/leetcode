from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 0
        points.sort(key=lambda x:x[1])
        curR = points[0][1]
        for i in range(1,len(points)):
            if points[i][0]<=curR:
                ans+=1
            else:
                curR = points[i][1]
        return len(points)-ans


if __name__ == '__main__':
    s = Solution()
    print(s.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))