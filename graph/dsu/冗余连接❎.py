class Solution:
    """
    合法的树---所有节点都是连通的
    原来是环 如果删除一条边后，所有节点还是连通的，那么就可以删除
    对于边 f-t,如果f，t已经是连通的，加入这条边，那么就会成环了！
    从前向后遍历边，就可以按要求输出最后输入的冗余边
    """
    def fn(self):
        n = int(input())
        father = [i for i in range(n+1)]
        edges = []
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
        for i in range(n):
            f,t = map(int,input().split())
            if is_same(f,t):
                print(f'{f} {t}')
                break
            union(f,t)



if __name__ == '__main__':
    s = Solution()
    while True:
        try:
            s.fn()
        except Exception:
            break