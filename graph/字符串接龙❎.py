from collections import deque
from typing import List


class Solution:
    """
    两个要素 1.如何对strList进行连接 2.如何求最短路径
    对于1，其实就是基于构造strList+begin+end构造一张无权、无向图，两个节点如果只有一个字母不同，那么就可以进行修改，所以这样的节点是连通的
    对于2 ，BFS是求最短路径的最佳方案
    """
    def fn(self,start,end,strList:List[str]):
        def can_connected(s1,s2):
            """判断s1和s2是否可以连通"""
            differ = 0
            for i in range(len(s1)):
                if s1[i]!=s2[i]:
                    differ+=1
                if differ>1:
                    return False
            return True
        # bfs (str,path_length)
        q = deque([(start,1)])
        visited = set()
        while q:
            # 判断是否可以连通end
            cur,length = q.popleft()
            if can_connected(cur,end):
                return length+1
            # 逐个和其他节点尝试连接
            for v in strList:
                if v not in visited and can_connected(cur,v):
                    visited.add(v)
                    q.append((v,length+1))
        return 0

if __name__ == '__main__':
    so = Solution()
    while True:
        try:
            n = int(input())
            start,end = map(str,input().split())
            strList = []
            for i in range(n):
                strList.append(input())
            print(so.fn(start,end,strList))
        except EOFError:
            break