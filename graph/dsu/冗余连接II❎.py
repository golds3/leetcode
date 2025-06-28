class Solution:
    """
    要求是有向的，那么满足 只有根节点的入度是0，其他节点的入读是1，造成冗余边的节点入度是2，所以找到入度为2的节点的边就好了
    对于入度为2 有两种情况
    1.无论删除哪条，删除后都是有向树，删除靠后的就行
    2.只能删除特定的边，才能保证是有向树
    情况三，图中没有入度为2的节点，那么说明整个图成环了，那么就要删除构成环的边
    """
    def fn(self):
        n = int(input())
        father = [i for i in range(n+1)]
        in_degree = [0 for i in range(n+1)]
        possible_edges = []
        edges = []
        for i in range(n):
            f,t = map(int,input().split())
            edges.append((f,t))
            in_degree[t] +=1

        for v in edges:
            if in_degree[v[1]] == 2:
                possible_edges.append((v[0],v[1]))

        def find(v):
            if v == father[v]:
                return v
            father[v] = find(father[v])
            return father[v]
        def union(u,v):
            u = find(u)
            v = find(v)
            if u==v: return
            father[v] = u
        def is_same(v,u):
            return find(v) == find(u)
        if not possible_edges:
            # 成环了
            for v in edges:
                f,t = v
                if is_same(f,t):
                    print(f'{f} {t}')
                    break
                union(t,f)
            return
        # 从后往前尝试删除
        remove = possible_edges[-1]
        for v in edges:
            if remove == v:
                continue
            f,t = v
            if is_same(f,t):
                # 成环了，说明不能删
                print(f'{possible_edges[0][0]} {possible_edges[0][1]}')
                return
            union(t,f)
        print(f'{remove[0]} {remove[1]}')








if __name__ == '__main__':
    s = Solution()
    while True:
        try:
            s.fn()
        except Exception:
            break