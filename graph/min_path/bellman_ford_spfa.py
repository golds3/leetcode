from collections import deque
from typing import List


class BellmanFordSpfa:
    """
    BellmanFord 的队列优化算法
    """
    def fn(self,edges:List[List[tuple]],start,end,n):
        min_dist = [float('inf')]*(n+1)
        min_dist[start] = 0
        q = deque([start])
        visited = [False]*(n+1) # 防止重复入队列
        # 松弛n-1次
        while q:
            cur = q.popleft()
            visited[cur] = False # 保证cur后面发生了改变可以入队
            min_dist_copy = min_dist.copy()# 记录上一轮松弛的结果
            for t,v in edges[cur]:
                if  min_dist_copy[cur]!=float('inf') and min_dist_copy[cur]+v < min_dist[t]:
                    min_dist[t] = min_dist_copy[cur]+v
                    if not visited[t]:
                        q.append(t)
                        visited[t] = True
        if min_dist[end]==float('inf'):
            return "unconnected"
        else:
            return min_dist[end]

if __name__ == '__main__':
    s = BellmanFordSpfa()
    while True:
        try:
            n,edge = map(int,input().split())
            grid = [[] for _ in range(n+1)]
            for _ in range(edge):
                f,t,v = map(int,input().split())
                #因为队列的方式我们已经知道当前节点是谁了，所以用邻接表更快，不用遍历边集合了
                grid[f].append((t,v))
                # grid.append((f,t,v))
            print(s.fn(grid,1,n,n))
        except Exception as e:
            break