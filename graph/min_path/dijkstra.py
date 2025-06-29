import sys
from typing import List


class Dijkstra:
    """
    朴素版，以节点的角度实现
    """
    def fn(self,graph:List[List[int]]):
        """
        graph: 邻接矩阵
        """
        min_dist = [sys.maxsize-1]*(len(graph)) # 源点到其他点的距离
        visited = [False]*(len(graph)+1)
        parent = [0 for _ in range(len(graph))] # 用于打印路径
        min_dist[1] = 0 # 源点到源点的距离为0
        for _ in range(1,len(graph)):
            min_distance = sys.maxsize
            cur = 0
            #step1 选取距离源点最近的节点，且未访问过
            for i in range(1,len(graph)):
                if not visited[i] and min_dist[i] < min_distance:
                    cur = i
                    min_distance = min_dist[i]
            # step2 标记节点
            visited[cur] = True
            # step3 更新min_dist 数组
            for i in range(1,len(graph)):
                if not visited[i] and min_dist[cur]+graph[cur][i] < min_dist[i]:
                    min_dist[i] = min_dist[cur]+graph[cur][i]
                    parent[i] = cur
        if min_dist[-1] == sys.maxsize-1:
            return -1 # 无法从起点到达终点
        else:
            for i in range(1,len(parent)):
                print(f'{parent[i]}->{i}')
            return min_dist[-1]






if __name__ == '__main__':
    s = Dijkstra()
    while True:
        try:
            n,edges =map(int,input().split())
            graph = [[sys.maxsize-1 for _ in range(n+1)] for _ in range(n+1)]
            for _ in range(edges):
                f,t,w = map(int,input().split())
                graph[f][t] = w
            print(s.fn(graph))
        except Exception as e:
            break