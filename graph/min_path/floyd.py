class Floyd:
    def fn(self):
        n,edges = map(int,input().split())
        # grid[i][j][k] = m，表示 节点i 到 节点j 以在[1,k]中选一个为中间节点的最短距离为m。
        graph = [[[float('inf')]*(n+1) for _ in range(n+1)]for _ in range(n+1)]
        # 初始化 第0层 ,i到j不经过任何中间节点
        for _ in range(edges):
            f,t,w = map(int,input().split())
            graph[f][t][0] = w
            graph[t][f][0] = w
        start_count = int(input())
        query = []
        for _ in range(start_count):
            start,end = map(int,input().split())
            query.append((start,end))

        for k in range(1,n+1):
            for i in range(1,n+1):
                for j in range(1,n+1):
                    # 选择经过k or 不选择k
                    graph[i][j][k] = min(graph[i][k][k-1]+graph[k][j][k-1],graph[i][j][k-1])
        for start,end in query:
            if graph[start][end][n] == float('inf'):
                print(-1)
            else:
                print(graph[start][end][n])

    def fn_2(self):
        n,edges = map(int,input().split())
        # grid[i][j] = m，表示 节点i 到 节点j 以在[1,k]中选一个为中间节点的最短距离为m。
        graph = [[float('inf') for _ in range(n+1)]for _ in range(n+1)]
        # 初始化 第0层 ,i到j不经过任何中间节点
        for _ in range(edges):
            f,t,w = map(int,input().split())
            graph[f][t] = w
            graph[t][f] = w
        start_count = int(input())
        query = []
        for _ in range(start_count):
            start,end = map(int,input().split())
            query.append((start,end))

        for k in range(1,n+1):
            for i in range(1,n+1):
                for j in range(1,n+1):
                    # 选择经过k or 不选择k
                    graph[i][j] = min(graph[i][k]+graph[k][j],graph[i][j])
        for start,end in query:
            if graph[start][end] == float('inf'):
                print(-1)
            else:
                print(graph[start][end][n])

if __name__ == '__main__':
    s = Floyd()
    while True:
        try:
            s.fn()
        except Exception:
            break
