class Edge:
    def __init__(self,f,t,v):
        self.f = f
        self.t = t
        self.v = v


class Kruskal:
    def fn(self,n,edges):
        father = [i for i in range(n+1)]
        in_tree = []
        result = 0
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
            if u == v:
                return
            father[v] = u
        # step 1 sort by value
        edges.sort(key=lambda x: x.v)
        # step2 choose
        for edge in edges:
            if is_same(edge.f,edge.t):
                # 成环，不可选
                continue
            union(edge.f,edge.t)
            in_tree.append(edge)
            result+=edge.v
        for edge in in_tree:
            print(f'{edge.f}->{edge.t}')
        return result

if __name__ == '__main__':
    so = Kruskal()
    while True:
        try:
            v,e = map(int,input().split())
            edges = []
            for _ in range(e):
                f,t,val = map(int,input().split())
                edges.append(Edge(f,t,val))
            print(so.fn(v,edges))
        except Exception as e:
            break
