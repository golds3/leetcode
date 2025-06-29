import sys
from typing import List


class Prim:
    def fn(self,graph):
        # 这里的graph使用邻接矩阵构建
        in_tree = [False for _ in range(len(graph))] # 最小生成树
        min_dist = [sys.maxsize-1 for _ in range(len(graph))] # min_dist 数组 记录i到最小生成树的最近距离
        parent = [0]*(len(graph)) # 用与打印最小生成树的路径

        # n 个节点，只需要构建n-1条边
        for _ in range(1,len(graph)-1):
            cur = 0 # 当前节点
            min_distance = sys.maxsize #距离最小生成树最近的距离
            # 循环进行prim算法
            for i in range(1,len(graph)):
                # step 1 挑选距离最小生成树最进的节点
                if not in_tree[i] and min_dist[i]<min_distance:
                    cur = i
                    min_distance = min_dist[i]
            # step2 加入最小生成树
            in_tree[cur] = True
            # step3 更新min_dis 数组
            for i in range(1,len(graph)):
                if not in_tree[i] and graph[cur][i]<min_dist[i]:
                    min_dist[i] = graph[cur][i]
                    parent[i] = cur
        # 打印最小生成树
        for i in range(1,len(parent)):
            print(f'{parent[i]}->+{i}')
        #最短路径
        return sum(min_dist[2:])

    """
    使用邻接表
    """
    def fn_2(self,graph:List[tuple]):
        # 这里的graph使用邻接矩阵构建
        in_tree = [False for _ in range(len(graph))] # 最小生成树
        min_dist = [sys.maxsize-1 for _ in range(len(graph))] # min_dist 数组 记录i到最小生成树的最近距离
        parent = [0]*(len(graph)) # 用与打印最小生成树的路径

        # n 个节点，只需要构建n-1条边
        for _ in range(1,len(graph)-1):
            cur = 0 # 当前节点
            min_distance = sys.maxsize #距离最小生成树最近的距离
            # 循环进行prim算法
            for i in range(1,len(graph)):
                # step 1 挑选距离最小生成树最进的节点
                if not in_tree[i] and min_dist[i]<min_distance:
                    cur = i
                    min_distance = min_dist[i]
            # step2 加入最小生成树
            in_tree[cur] = True
            # step3 更新min_dis 数组
            for vv in graph[cur]:
                node,val = vv
                if not in_tree[node] and val<min_dist[node]:
                    min_dist[node] = val
                    parent[node] = cur
        # 打印最小生成树
        for i in range(1,len(parent)):
            print(f'{i}->+{parent[i]}')
        #最短路径
        return sum(min_dist[2:])

if __name__ == '__main__':
    so = Prim()
    while True:
        try:
            v,e = map(int,input().split())
            graph = [[sys.maxsize-1]*(v+1) for _ in range(v+1)]
            graph_2 = [[] for _ in range(v+1)]
            for i in range(e):
                f,t,s = map(int,input().split())
                graph[f][t] = s
                graph[t][f] = s
                graph_2[f].append((t,s))
                graph_2[t].append((f,s))
            print(so.fn(graph))
            print(so.fn_2(graph_2))
        except Exception as e:
            e.with_traceback()
            break
