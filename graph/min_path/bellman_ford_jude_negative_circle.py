from typing import List


class BellmanFord:
    """
    判断 是否存在负权回路
    """
    def fn(self,edges:List[tuple],start,end,n):
        min_dist = [float('inf')]*(n+1)
        min_dist[start] = 0
        # 松弛n-1次
        for _ in range(1,n):
            update=False
            min_dist_copy = min_dist.copy() # 记录上一轮松弛的结果
            for f,t,v in edges:
                if min_dist_copy[f]!=float('inf') and min_dist_copy[f]+v < min_dist[t]:
                    min_dist[t] = min_dist_copy[f]+v
                    update = True
            if not update: # 如果所有边松弛完后都没有发生变化，就可以提前结束了
                break
        # 再进行一次松弛
        for f,t,v in edges:
            if min_dist[f]!=float('inf') and min_dist[f]+v < min_dist[t]:
                return "circle"
        if min_dist[end]==float('inf'):
            return "unconnected"
        else:
            return min_dist[end]




if __name__ == '__main__':
    s = BellmanFord()
    while True:
        try:
            n,edge = map(int,input().split())
            grid = []
            for _ in range(edge):
                f,t,v = map(int,input().split())
                grid.append((f,t,v))
            print(s.fn(grid,1,n,n))
        except Exception as e:
            break