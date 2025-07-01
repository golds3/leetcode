from typing import List


class BellmanFordLimit:
    """
    单源有限
    """
    def fn(self,edges:List[tuple],start,end,step,n):
        min_dist = [float('inf')]*(n+1)
        min_dist[start] = 0
        # 松弛n-1次
        for _ in range(step+1):
            update=False
            min_dist_copy = min_dist.copy()
            for f,t,v in edges:
                if min_dist_copy[f]!=float('inf') and min_dist_copy[f]+v < min_dist[t]:
                    min_dist[t] = min_dist_copy[f]+v
                    update = True
            if not update: # 如果所有边松弛完后都没有发生变化，就可以提前结束了
                break
        if min_dist[end]==float('inf'):
            return "unreachable"
        else:
            return min_dist[end]




if __name__ == '__main__':
    s = BellmanFordLimit()
    while True:
        try:
            n,edge = map(int,input().split())
            grid = []
            for _ in range(edge):
                f,t,v = map(int,input().split())
                grid.append((f,t,v))
            start,end,k = map(int,input().split())
            print(s.fn(grid,start,end,k,n))
        except Exception as e:
            break