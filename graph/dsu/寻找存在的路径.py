class Solution:
    def fn(self,grid,start,end):
        # 判断start和end是否连通---并查集
        father = [i for i in range(len(grid))]
        def find(v):
            if father[v] == v:
                return v
            father[v] = find(father[v])
            return father[v]
        def is_same(u,v):
            return find(u) == find(v)
        def union(u,v):
            u = find(u)
            v = find(v)
            if u==v:
                return
            father[v] = u
        for i in range(1,len(grid)):
            for v in grid[i]:
                union(i,v)
        if is_same(start,end):
            return 1
        else:
            return 0





if __name__ == '__main__':
    so = Solution()
    while True:
        try:
            n,edge = map(int,input().split())
            grid = [[] for _ in range(n+1)]
            for i in range(edge):
                f,t = map(int,input().split())
                # 无向图
                grid[f].append(t)
                grid[t].append(f)
            start,end = map(int,input().split())
            print(so.fn(grid,start,end))
        except EOFError as e:
            break