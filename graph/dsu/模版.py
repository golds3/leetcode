class DSUPathCompression:
    """
    使用路径压缩进行优化的 并查集
    """
    def __init__(self, n):
        """
        :param n: 节点个数
        """
        self.father = [i for i in range(n)] #初始化，每个节点的根都是自己

    def find(self,u):
        """
        查找 u 的根，并在查找的过程进行路径压缩
        :return:
        """
        if self.father[u] == u:
            return u

        # 路径压缩
        self.father[u] = self.find(self.father[u])
        return self.father[u]

    def is_same(self, u, v):
        """
        判断u 和 v 是否连通(在同一个集合中)
        :param u:
        :param v:
        :return:
        """
        fu = self.find(u)
        fv = self.find(v)
        return fu == fv

    def union(self, u, v):
        """
        把u和v加入到集合中，如果原来是不在集合中的，那么将u，v连通，两者的根节点为 u
        :param u:
        :param v:
        :return:
        """
        fu = self.find(u)
        fv = self.find(v)
        if fu == fv:
            return
        # union
        self.father[fv] = fu


class DSURankUnion:
    """
    使用秩合并进行优化的 并查集
    """

    def __init__(self, n):
        """
        :param n: 节点个数
        """
        self.father = [i for i in range(n)]  # 初始化，每个节点的根都是自己
        self.rank = [1 for i in range(n)] # 每个节点的高度初始化为1

    def find(self, u):
        """
        查找 u 的根
        :return:
        """
        if self.father[u] == u:
            return u
        return self.find(self.father[u])

    def is_same(self, u, v):
        """
        判断u 和 v 是否连通(在同一个集合中)
        :param u:
        :param v:
        :return:
        """
        fu = self.find(u)
        fv = self.find(v)
        return fu == fv

    def union(self, u, v):
        """
        把u和v加入到集合中，如果原来是不在集合中的，那么将u，v连通，两者的根节点为 u
        并对u，v进行秩合并，把rank小的合并到rank大的树中
        :param u:
        :param v:
        :return:
        """
        fu = self.find(u)
        fv = self.find(v)
        # 秩合并
        if self.rank[fu] <= self.rank[fv]:
            self.father[fu] = fv
            if self.rank[fu] == self.rank[fv] and fu!=fv:
                self.rank[fv]+=1
        else:
            self.father[fv] = fu




