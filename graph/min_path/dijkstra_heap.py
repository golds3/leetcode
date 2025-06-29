import heapq
import sys
from typing import List

class Edge:
    def __init__(self,t,v):
        self.t = t
        self.v = v

class DijkstraHeap:
    """
    Dijkstra 的堆优化方案
    使用小顶堆，以边的维度实现
    """
    def fn(self,graph:List[List[int]]):
        """
        graph: 邻接表
        """
        min_heap = []
        min_dist = [sys.maxsize for _ in range(len(graph))]
        visited = [False for _ in range(len(graph))]
        min_dist[1] = 0
        heapq.heappush(min_heap,(0,1)) # 按照权值排序
        parent = [0]*(len(graph)) # 存储路径
        while min_heap:
            # step1 选取离源点最近的点
            val,cur = heapq.heappop(min_heap)
            # step2 标记节点
            visited[cur] = True
            # step 3 更新min_dist
            for vv in graph[cur]:
                i,v = vv.t,vv.v
                if not visited[i] and val + v < min_dist[i]:
                    min_dist[i] = min_dist[cur] + v
                    heapq.heappush(min_heap,(min_dist[i],i))
                    parent[i] = cur
        if min_dist[-1]==sys.maxsize:
            return -1
        else:
            for i in range(1,len(parent)):
                print(f'{parent[i]}->{i}')
            return min_dist[-1]



if __name__ == '__main__':
    s = DijkstraHeap()
    while True:
        try:
            n,edges =map(int,input().split())
            graph = [[] for _ in range(n+1)]
            for _ in range(edges):
                f,t,w = map(int,input().split())
                graph[f].append(Edge(t,w))
            print(s.fn(graph))
        except Exception as e:
            break